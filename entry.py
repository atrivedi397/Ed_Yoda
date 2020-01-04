from db_connection import *


class OldPeople:
    def __init__(self, name, spouse, fund):
        self.name = name
        self.spouse = spouse
        self.fund = fund
        self.availability = "Yes"
        self.taken_care_by = None
        self.requested_by = []
        self.reviews = {}
        self.ratings = {}

    def enter_in_db(self):
        old_Table.insert_one({"name": self.name, "spouse": self.spouse, "requested_by": self.requested_by,
                              "fund": self.fund, "availability": self.availability, "taken_care_by": self.taken_care_by,
                              "reviews": self.reviews, "rating": self.ratings})

    def rate_and_reviews(self, given_to_young_person):
        self.ratings[given_to_young_person] = int(input(f"How do you rate {given_to_young_person} out of 5?\n"))
        self.reviews[given_to_young_person] = input(f"What is you review about {given_to_young_person}?\n")
        ratings, reviews = "ratings." + str(given_to_young_person), "reviews." + str(given_to_young_person)
        old_Table.update_one({"name": self.name}, {"$set": {ratings: self.ratings, reviews: self.reviews}})

    @staticmethod
    def oldies_available():
        cursor = old_Table.find({"availability": "Yes"}, {"name": 1, "_id": 0})
        if cursor is not None:
            for value in cursor:
                print(value)
        else:
            print("All elders are occupied")

    @staticmethod
    def show_details(name):
        cursor = old_Table.find_one({"name": name})
        for value in cursor:
            print(value, " : ", cursor[value])


class YoungPeople:
    def __init__(self, name):
        self.name = name
        self.taking_care_of = []
        self.requested_oldies = []
        self.ratings = {}
        self.reviews = {}

    def rate_and_reviews(self, given_to_old_person):
        self.ratings[given_to_old_person] = int(input(f"How do you rate {given_to_old_person} out of 5?\n"))
        self.reviews[given_to_old_person] = input(f"What is you review about {given_to_old_person}?\n")
        ratings, reviews = "ratings." + str(given_to_old_person), "reviews." + str(given_to_old_person)
        young_Table.update_one({"name": self.name}, {"$set": {ratings: self.ratings, reviews: self.reviews}})

    def enter_in_db(self):
        young_Table.insert_one({"name": self.name, "taking_care_of": self.taking_care_of,
                                "requested_oldies": self.requested_oldies,
                                "ratings": self.ratings, "reviews": self.reviews})

    def want_to_take_care_list(self):
        return young_Table.find_one({"name": self.name}, {"_id": 0, "requested_oldies": 1, "name": 1})

    @staticmethod
    def show_details(name):
        cursor = young_Table.find_one({"name": name})
        for value in cursor:
            print(value, " : ", cursor[value])
