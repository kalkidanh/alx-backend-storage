#!/usr/bin/env python3
""" Class that stores a Redis client as a private variable"""

from typing import Union
from uuid import uuid4
import redis


class Cache():
    """ Defines the class 'Cache' """

    def __init__(self):
        """ Initializes the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that generate a random key, store the input data in Redis
        Args:
            data (Union[str, bytes, int, float]): The argument
        Returns:
            str: return the key
        """
        generate_random_key = str(uuid4())
        self._redis.set(generate_random_key, data)
        return generate_random_key
