#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 30-01-2024
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """implements FIFO caching algorithm"""

    def __init__(self):
        super().__init__()
        # keeps track of first key added
        self.__fifolist = []

    def put(self, key, item):
        """
        place key value pares in caching_items
        if caching items is full then evict the first item
        """
        if (key is not None and item is not None):
            self.__fifolist.append(key)
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                val = self.__fifolist.pop(0)
                self.cache_data.pop(val)
                print(f"DISCARD: {val}")

    def get(self, key):
        """returns respective data from key in cache_items property"""
        return self.cache_data.get(key)


if __name__ == '__main__':
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
