import collections
import datetime
from multiprocessing import pool


class DistributedLRUCache:
    """Simple LRU cache implemented using ordered dictionary to keep track of last used"""
    # Implemented points 1, 3, 4, 6
    # 1 - This implementation require no 3rd party packages. All resources are built in
    # 2 - resilient to network failures could be done by backing up the cache every so often
    # 3 - Dictionaries are hashmaps, this gives average O(1) time of reading and writing
    # 4 - Having methods to merge dictionaries between two different caches ensure data consistency in the cache
    # 5 - Locality reference can be done by having a large hash distributed across regions and have clients compute
    #     a hash to determine which server to use. This gives a simple form of scalable sharding
    # 6 - Dictionary values can be of any time, however keys must be immutable. This should be flexible for most uses
    # 7 - Cache can expire on a timeout. However cache will be cleared only at the next mutating operation, and may
    #     still claim memory before that
    def __init__(self, size, timeout):
        """constructor"""
        self.size = size
        self.cache = collections.OrderedDict()
        self.timeout = timeout
        self.lastAccess = datetime.datetime.now()

    def get(self, key):
        """get value corresponding to key, move pair to front. -1 if it does not exist"""
        try:
            self.expired()
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        """add key and value to dict. Remove last if full"""
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)
        self.cache[key] = value

    def join(self, other):
        """join two cache together"""
        self.cache = {**self.cache, **other.cache}

    def expired(self):
        """clear cache if exceeds timeout"""
        if self.lastAccess + datetime.timedelta(seconds=self.timeout) < datetime.datetime.now():
            self.clear()

    def display(self):
        """print all key value pairs"""
        for key, value in self.cache.items():
            print(key, value)

    def clear(self):
        """clears cache"""
        self.cache.clear()


cache1 = DistributedLRUCache(5, 300)
cache2 = DistributedLRUCache(5, 300)
cache1.set(1, 1)
cache1.set(2, 2)
cache2.set(3, 3)
cache2.set(4, 4)
cache1.join(cache2)
cache1.display()
