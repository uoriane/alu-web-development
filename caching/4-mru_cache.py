#!/usr/bin/python3
""" MRUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines an MRU caching system.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru_key = None

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            self.mru_key = key
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.mru_key in self.cache_data:
                del self.cache_data[self.mru_key]
                print(f"DISCARD: {self.mru_key}")
            else:
                mru_k, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {mru_k}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)
        self.mru_key = key

    def get(self, key):
        """ Get an item by key and mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        self.mru_key = key
        return self.cache_data.get(key)
