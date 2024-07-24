#!/usr/bin/env python3
"""
Module 0-basic_cache

Contains a class BasicCache that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """Adds an item to the cache dictionary with the given key and value"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the value associated with the given key from the cache_data
        dictionary.
        """
        return self.cache_data.get(key, None)
