#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 30-01-2024
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """implements LIFO caching algorithm"""

    def __init__(self):
        super().__init__()
        # keeps track of first key added
        self.__lifoitem = ""

    def put(self, key, item):
        """
        place key value pares in caching_items
        if caching items is full then evict the last item
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                self.cache_data.pop(self.__lifoitem)
                print(f"DISCARD: {self.__lifoitem}")
            self.__lifoitem = key

    def get(self, key):
        """returns respective data from key in cache_items property"""
        return self.cache_data.get(key)


if __name__ == '__main__':
    my_cache = LIFOCache()
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
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
