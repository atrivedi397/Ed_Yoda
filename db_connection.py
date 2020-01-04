from pymongo import MongoClient
client = MongoClient("localhost", 27017)

# used database
db = client["CareGiving"]

old_Table = db["old_people_collection"]
young_Table = db["young_people_collection"]
