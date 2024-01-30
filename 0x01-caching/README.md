# Caching Algorithms

Cache is a hardware or software that allows for temporary storage of recently or frequently accessed data which increases the speed of the way in which data is accessed. To increase the efficiency of caching, cache replacement algorithms are used

## Learning Objectives

* What a caching system is
* What FIFO means
* What LIFO means
* What LRU means
* What MRU means
* What LFU means
* What the purpose of a caching system
* What limits a caching system have

## Tasks

* [0-basic_cache.py](0-basic_cache.py) - Create a class BasicCache that inherits from BaseCaching and is a caching system:
  * You must use self.cache_data - dictionary from the parent class BaseCaching
  * This caching system doesn’t have limit
  * `def put(self, key, item)`:
    * Must assign to the dictionary self.cache_data the item value for the key key.
    * If key or item is None, this method should not do anything.
  * `def get(self, key)`:
    * Must return the value in self.cache_data linked to key.
    * If key is None or if the key doesn’t exist in self.cache_data, return None.
