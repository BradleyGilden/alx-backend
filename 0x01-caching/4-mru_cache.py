#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 30-01-2024
"""
from base_caching import BaseCaching
from datetime import datetime


class MRUCache(BaseCaching):
    """implements MRU caching algorithm"""

    def __init__(self):
        """constructor of LRUCache"""
        super().__init__()
        # keeps track of key recency of all keys
        self.__mru = {}

    def put(self, key, item):
        """
        place key value pares in caching_items
        if caching items is full then evict the most recently used item
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                # find least recenty used time
                maxval = max(self.__mru.values())
                copy = self.__mru.copy()
                for k, v in copy.items():
                    if (v == maxval):
                        del self.cache_data[k]
                        del self.__mru[k]
                        print(f"DISCARD: {k}")
                        break
            self.__mru[key] = datetime.utcnow()

    def get(self, key):
        """returns respective data from key in cache_items property"""
        if (key in self.cache_data):
            self.__mru[key] = datetime.utcnow()

        return self.cache_data.get(key)


if __name__ == '__main__':
    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
