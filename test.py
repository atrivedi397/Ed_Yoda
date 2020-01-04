import unittest
from make_requests_and_approve import *

# Tests for the given 2 questions


class Test(unittest.TestCase):
    def test_people_taking_care_elders(self):
        self.assertEqual(all_people_being_taken_care(), [{'name': 'Hari P.', 'taken_care_by': 'ravish'},
                                                         {'name': 'abc', 'taken_care_by': 'ravish'},
                                                         {'name': 'def', 'taken_care_by': 'ravish'},
                                                         {'name': 'ghi', 'taken_care_by': 'ravish'},
                                                         {'name': 'jkl', 'taken_care_by': 'sudhir'}], "Correct")

    def test_sum_tuple(self):
        names = ["ravish", "sudhir", "arnab"]
        outputs = [[{'name': 'ravish', 'taking_care_of': ['abc', 'Hari P.', 'def', 'ghi']}],
                   [{'name': 'sudhir', 'taking_care_of': ['jkl']}],
                   [{'name': 'arnab', 'taking_care_of': []}]]
        for name, output in zip(names, outputs):
            self.assertEqual(young_person_taking_care_of(name), output, "Correct")


if __name__ == '__main__':
    unittest.main()
