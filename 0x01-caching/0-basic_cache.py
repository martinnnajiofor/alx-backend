#!/usr/bin/python3
''' Create a class BasicCache that inherits from BaseCaching and is a caching system
'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' A basic cache.
        Inherits from class BaseCaching.
        Attributes:
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache
    '''

    def put(self, key, item):
        ''' Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything. '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None. '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
