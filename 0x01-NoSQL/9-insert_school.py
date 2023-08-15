#!/usr/bin/env python3
""" Function that inserts a new document in a collection using kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection using kwargs

    Args:
        mongo_collection (_type_): pymongo collection object
    Returns:
        Id: new id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
