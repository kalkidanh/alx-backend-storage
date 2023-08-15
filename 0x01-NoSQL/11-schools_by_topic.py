#!/usr/bin/env python3
""" Function that returns the list of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """ Define the list of schools having a specific topic

    Args:
        mongo_collection (_type_): pymongo collection object
        topic (str): topic searched
    Returns:
        List: the list of school with a specific topic
    """
    return mongo_collection.find({"topics": topic})
