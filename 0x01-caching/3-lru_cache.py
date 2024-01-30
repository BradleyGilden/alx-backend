#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 30-01-2024
"""
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """implements LRU caching algorithm"""

    def __init__(self):
        """constructor of LRUCache"""
        super().__init__()
        # keeps track of key recency of all keys
        self.__lru = {}

    def put(self, key, item):
        """
        place key value pares in caching_items
        if caching items is full then evict the least recently used item
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item
            self.__lru[key] = datetime.utcnow()

            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                # find least recenty used time
                minval = min(self.__lru.values())
                copy = self.__lru.copy()
                for k, v in copy.items():
                    if (v == minval):
                        del self.cache_data[k]
                        del self.__lru[k]
                        print(f"DISCARD: {k}")
                        break

    def get(self, key):
        """returns respective data from key in cache_items property"""
        if (key in self.cache_data):
            self.__lru[key] = datetime.utcnow()

        return self.cache_data.get(key)


if __name__ == '__main__':
    my_cache = LRUCache()
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

"""
a 0
b 1
c 3
d 2
"""
