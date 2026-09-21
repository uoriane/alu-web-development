#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
