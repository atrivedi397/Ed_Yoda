from make_requests_and_approve import *

old_person = OldPeople(None, None, 0)
young_person = YoungPeople(None)


if __name__ == "__main__":
    while True:

        action = int(input("\nWhat do you want to do?"
                           "\n1. Register Elders"
                           "\n2. Give rating as Elder person"
                           "\n3. Register Younger"
                           "\n4. Give rating and review as caretaker"
                           "\n5. Check for any Young person"
                           "\n6. Check for any Elderly Person"
                           "\n7. Make a request as Young Person"
                           "\n8. Approve a person to take care"
                           "\n9. List all available people"
                           "\n10. Show details of Young person"
                           "\n11. Show details of Old Person"
                           "\n12. All Oldies which are taken care by any person"
                           "\n13. Exit\n\n"))

        if action == 1:
            print("Provide the following details for old person to register\n")
            name = input("Provide the name of the person\n")
            spouse = input("Provide the name of spouse of the person\n")
            fund = int(input("Provide the fund in numeric to add\n"))
            old_person = OldPeople(name, spouse, fund)
            old_person.enter_in_db()

        elif action == 2:
            name = input("Provide the name of the elder person\n")
            to_young = input("Provide the name of the care taker person\n")
            cursor = old_Table.find_one({"name": name})
            old_obj = OldPeople(cursor["name"], cursor["spouse"], cursor["fund"])
            old_obj.rate_and_reviews(to_young)

        elif action == 3:
            print("Provide the following details for young person to register\n")
            name = input("Provide the name of the person\n")
            young_person = YoungPeople(name)
            young_person.enter_in_db()

        elif action == 4:
            name = input("Provide the name of the young person\n")
            to_old = input("Provide the name of the person who is looked after\n")
            cursor = young_Table.find_one({"name": name})
            young_obj = YoungPeople(cursor["name"])
            young_obj.rate_and_reviews(to_old)

        elif action == 5:
            name = input("Provide the name of the young person\n")
            taking_care(name)

        elif action == 6:
            name = input("Provide the name of the old person\n")
            taken_care(name)

        elif action == 7:
            name = input("Provide the name of the young person\n")
            to_old = input(f"Provide the name of the person who is looked after from {old_person.oldies_available()}\n")
            make_request(name, to_old)

        elif action == 8:
            approval_by_old_person()

        elif action == 9:
            print(old_person.oldies_available())

        elif action == 10:
            name = input("Provide the name of the young person\n")
            young_person.show_details(name)

        elif action == 11:
            name = input("Provide the name of the old person\n")
            old_person.show_details(name)

        elif action == 12:
            print(all_people_being_taken_care())

        elif action == 13:
            print("Thank You")
            exit(0)
