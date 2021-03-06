from entry import *


# function for making request for taking care of old person
def make_request(young_name, old_name):
    cursor = young_Table.find_one({"name": young_name}, {"_id": 0, "taking_care_of": 1})
    if len(cursor["taking_care_of"]) < 4:
        young_Table.update_one({"name": young_name}, {"$push": {"requested_oldies": old_name}})
        old_Table.update_one({"name": old_name}, {"$push": {"requested_by": young_name}})
    else:
        print("Sorry, The young lad is already taking care of 4 people.")


# function making approval by old person for the young folk
def approval_by_old_person():
    old_human = input("Please provide your name\n")
    cursor = old_Table.find_one({"name": old_human}, {"requested_by": 1, "_id": 0})
    all_requesting_to_take_care = list(cursor["requested_by"])

    for name in all_requesting_to_take_care:
        young_cursor = young_Table.find_one({"name": name}, {"_id": 0, "taking_care_of": 1})
        if len(young_cursor["taking_care_of"]) >= 4:
            all_requesting_to_take_care.remove(name)

    if len(all_requesting_to_take_care) != 0:
        approved_person = input(f"Please type the name from {all_requesting_to_take_care}\n")
        old_Table.update_one({"name": old_human}, {"$set": {"taken_care_by": approved_person, "availability": "No"}})
        young_Table.update_one({"name": approved_person}, {"$push": {"taking_care_of": old_human}})
        young_Table.update_one({"name": approved_person}, {"$pull": {"requested_oldies": old_human}})

    else:
        print("\nEither No one requested to serve you or All people are serving at least 4 people")


def taken_care(old_person_name):
    cursor = old_Table.find_one({"name": old_person_name}, {"taken_care_by": 1})
    array = cursor["taken_care_by"]
    print(f"The {old_person_name} is looked after by {array}")


def taking_care(young_person_name):
    cursor = young_Table.find_one({"name": young_person_name}, {"taking_care_of": 1})
    array = cursor["taking_care_of"]
    print(f"The {young_person_name} is looking after {array}")


# function to find out all the people being currently taken care
def all_people_being_taken_care():
    cursor = old_Table.find({"availability": "No"}, {"_id": 0, "name": 1, "taken_care_by": 1})
    elder_list = []
    for value in cursor:
        elder_list.append(value)
    return elder_list


# function to find out a given young person is taking care of how many people
def young_person_taking_care_of(name):
    cursor = young_Table.find({"name": name}, {"_id": 0, "name": 1, "taking_care_of": 1})
    younger_list = []
    for value in cursor:
        younger_list.append(value)
    return younger_list
