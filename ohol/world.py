"""World/map data"""
import zlib

class Square:
    """One game square"""
    def __init__(self, biom=1, floors=0, t=0):
        self.biom = biom
        self.floors = floors
        self.t = t

    def __str__(self):
        """
        Format:
                            sscanf( tokens->getElementDirect(i),
                                    "%d:%d:%d",
                                    &( mMapBiomes[mapI] ),
                                    &( mMapFloors[mapI] ),
                                    &( mMap[mapI] ) );
                                    """
        return '{} {} {}'.format(self.biom, self.floors, self.t)


class Tile:
    def __init__(self, x, y, data=None):
        """One map tile, containing .size_x by size_y `ohol.world.Square`s"""
        self.size_x = 32
        self.size_y = 30
        self.x = x
        self.y = y
        self._data = data if data else []
        while len(self._data) < self.size_x * self.size_y:
            self._data.append(Square())
        self._cache_dirty = True
        self._cache = b''

    def __getitem__(self, pos):
        print(pos)

    def __setitem__(self, pos, value):
        pass

    def update_cache(self):
        ascii_data = self.ascii()
        compressed = zlib.compress(ascii_data)
        binary_raw_size = len(ascii_data)
        binary_compressed_size = len(compressed)
        header = 'MC\n{} {} {} {}\n{} {}\n#'
        header = header.format(self.size_x, self.size_y, self.x, self.y,
                             binary_raw_size, binary_compressed_size)
        self._cache = header.encode('ascii') + compressed

    def ascii(self):
        data = ' '.join(str(square) for square in self._data)
        return data.encode('ascii')

    def __bytes__(self):
        if self._cache_dirty:
            self.update_cache()

        return self._cache
