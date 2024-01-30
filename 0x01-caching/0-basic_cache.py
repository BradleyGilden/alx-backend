#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 30-01-2024
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a basic caching system with no limits"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assigns key value pairs to the cache_items property"""
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """returns respective data from key in cache_items property"""
        return self.cache_data.get(key)


if __name__ == '__main__':
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
