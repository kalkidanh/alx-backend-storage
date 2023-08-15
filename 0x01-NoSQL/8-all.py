#!/usr/bin/env python3
""" Function that lists all documents in a collection"""


def list_all(mongo_collection):
    """ Lists all documents in the collection

    Args:
        mongo_collection (_type_): Pymongo collection object
    Returns:
        List: A list of collections
    """
    return list(mongo_collection.find())
