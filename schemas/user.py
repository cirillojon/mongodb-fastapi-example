"""
This module defines the userEntity function which acts as a transformer for user data fetched from the MongoDB.
Its main purpose is to transform the MongoDB document into a more Python-friendly dictionary format, especially converting the '_id' field of MongoDB (which is an ObjectId) to a string format that can be easily used in the FastAPI application.

It is placed in the 'schemas' directory to indicate its role in shaping the data that moves between the application and the database.

Usage:
    Given a MongoDB user document `doc`, you can convert it using:
    `userEntity(doc)`

Structure:
    - The returned dictionary contains the following keys:
        - `id`: Corresponds to the MongoDB's '_id' and is converted to a string for easier handling.
        - `name`: The user's name.
        - `email`: The user's email address.
        - `password`: The user's password. Note: In a real-world application, storing plain-text passwords is discouraged. Always hash and salt passwords.
"""

def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "password":item["password"]   
    }

# `usersEntity` is a utility function designed to transform a list of user documents fetched from MongoDB.
# It makes use of the `userEntity` function to convert each individual document and then aggregates them into a list.
# This is especially useful when retrieving multiple user documents from the database and needing them in a consistent,
# Python-friendly format for the FastAPI application.
#
# Usage:
#     Given a list of MongoDB user documents `docs`, you can convert the entire list using:
#     `usersEntity(docs)`
#

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]