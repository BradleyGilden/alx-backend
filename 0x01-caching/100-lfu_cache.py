#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 30-01-2024
"""
from base_caching import BaseCaching
from datetime import datetime


class LFUCache(BaseCaching):
    """implements LRU caching algorithm"""

    def __init__(self):
        """constructor of LRUCache"""
        super().__init__()
        # keeps track of key recency
        self.__lru = {}
        # keeps track of key frequency
        self.__freq = {}

    def put(self, key, item):
        """
        place key value pares in caching_items
        if caching items is full then evict the least recently used item
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

            # if exceeded max space assigned
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                count = 0
                minlfu = min(self.__freq.values())
                lfucopy = self.__freq.copy()
                for v in lfucopy.values():
                    if (v == minlfu):
                        count += 1
                # if frequency is unique delete least frequently used
                if (count == 1):
                    for k, v in lfucopy.items():
                        if (v == minlfu):
                            del self.cache_data[k]
                            del self.__freq[k]
                            del self.__lru[k]
                            print(f"DISCARD: {k}")
                            break
                # get the lru if frequency is the same
                else:
                    lfu = {k: v for k, v in lfucopy.items() if v == minlfu}
                    lru = {k: v for k, v in self.__lru.items()
                           if k in lfu.keys()}
                    lrucopy = lru.copy()
                    minlru = min(lru.values())
                    for k, v in lrucopy.items():
                        if (v == minlru):
                            del self.cache_data[k]
                            del self.__freq[k]
                            del self.__lru[k]
                            print(f"DISCARD: {k}")
                            break
            if (key in self.__freq):
                self.__freq[key] += 1
            else:
                self.__freq[key] = 0
            self.__lru[key] = datetime.utcnow()

    def get(self, key):
        """returns respective data from key in cache_items property"""
        if (key in self.cache_data):
            self.__freq[key] += 1
            self.__lru[key] = datetime.utcnow()

        return self.cache_data.get(key)


if __name__ == '__main__':
    my_cache = LFUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
