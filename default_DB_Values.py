old_data = [{"name": "Hari P.", "spouse": "Shree", "requested_by": ["ravish"], "fund": 15000, "availability": "No",
             "taken_care_by": "ravish", "reviews": {}, "rating": {}},
            {"name": "abc", "spouse": "cba", "requested_by": ["ravish", "arnab"], "fund": 1200, "availability": "No",
             "taken_care_by": "ravish", "reviews": {}, "rating": {}},
            {"name": "def", "spouse": "fed", "requested_by": ["ravish"], "fund": 1300, "availability": "No",
             "taken_care_by": "ravish", "reviews": {}, "rating": {}},
            {"name": "ghi", "spouse": "ihg", "requested_by": ["ravish", "sudhir"], "fund": 1400, "availability": "No",
             "taken_care_by": "ravish", "reviews": {}, "rating": {}},
            {"name": "jkl", "spouse": "lkj", "requested_by": ["sudhir"], "fund": 1500, "availability": "No",
             "taken_care_by": "sudhir", "reviews": {}, "rating": {}},
            {"name": "mno", "spouse": "onm", "requested_by": ["sudhir"], "fund": 1600, "availability": "Yes",
             "taken_care_by": None, "reviews": {}, "rating": {}},
            {"name": "pqr", "spouse": "rqp", "requested_by": ["sudhir"], "fund": 1700, "availability": "Yes",
             "taken_care_by": None, "reviews": {}, "rating": {}},
            {"name": "stu", "spouse": "uts", "requested_by": ["sudhir"], "fund": 1800, "availability": "Yes",
             "taken_care_by": None, "reviews": {}, "rating": {}},
            {"name": "vwx", "spouse": "xwv", "requested_by": [], "fund": 1900, "availability": "Yes",
             "taken_care_by": None, "reviews": {}, "rating": {}},
            {"name": "yz", "spouse": "zy", "requested_by": ["arnab"], "fund": 2000, "availability": "Yes",
             "taken_care_by": None, "reviews": {}, "rating": {}}
            ]

young_data = [

    {"name": "ravish", "taking_care_of": ["abc", "Hari P.", "def", "ghi"], "requested_oldies": [], "ratings": {},
     "reviews": {}},
    {"name": "sudhir", "taking_care_of": ["jkl"], "requested_oldies": ["ghi", "mno", "pqr", "stu"], "ratings": {},
     "reviews": {}},
    {"name": "arnab", "taking_care_of": [], "requested_oldies": ["yz", "abc"], "ratings": {}, "reviews": {}}
    ]
