#!/usr/bin/env python3
"""
Generate a Canvas Common Cartridge (.imscc) import package for
CHM 125L - Life Chemistry Laboratory, Fall 2026.

Includes:
  - Weighted assignment groups (Quizzes 25%, Lab Reports 65%, Workshops 10%)
  - 9 empty quizzes, 9 empty lab report assignments, 3 empty workshop assignments
  - 15 weekly modules with assignments placed per the syllabus schedule
  - Custom grading standard matching the syllabus scale
"""

import os
import uuid
import zipfile
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(BASE, "_build")

COURSE_ID = "CHM125L_Fall2026"

ASSIGNMENT_GROUPS = [
    {"id": "ag_quizzes",     "title": "Quizzes",     "weight": 25, "position": 1},
    {"id": "ag_lab_reports", "title": "Lab Reports",  "weight": 65, "position": 2},
    {"id": "ag_workshops",   "title": "Workshops",    "weight": 10, "position": 3},
]

GRADING_SCALE = [
    ("A",  94.0, 100.0),
    ("A-", 90.0, 93.99),
    ("B+", 87.0, 89.99),
    ("B",  84.0, 86.99),
    ("B-", 80.0, 83.99),
    ("C+", 77.0, 79.99),
    ("C",  74.0, 76.99),
    ("C-", 70.0, 73.99),
    ("D+", 67.0, 69.99),
    ("D",  64.0, 66.99),
    ("D-", 61.0, 63.99),
    ("F",   0.0, 60.99),
]

WORKSHOPS = [
    {
        "id": "asgn_workshop_1",
        "title": "Workshop 1: Factor Labeling Method",
        "group": "ag_workshops",
        "points": 100,
        "due": "2026-09-14T13:15:00",
        "unlock": "2026-08-24T13:15:00",
        "description": "<p>Complete the Factor Labeling Method workshop packet. This workshop covers unit conversions and dimensional analysis essential for laboratory calculations.</p>",
        "submission_types": "online_upload,online_text_entry",
    },
    {
        "id": "asgn_workshop_2",
        "title": "Workshop 2: Shapes of Molecules",
        "group": "ag_workshops",
        "points": 100,
        "due": "2026-10-12T13:15:00",
        "unlock": "2026-09-28T13:15:00",
        "description": "<p>Complete the Shapes of Molecules workshop packet. This workshop covers VSEPR theory and molecular geometry.</p>",
        "submission_types": "online_upload,online_text_entry",
    },
    {
        "id": "asgn_workshop_3",
        "title": "Workshop 3: Writing/Balancing Reaction Equations",
        "group": "ag_workshops",
        "points": 100,
        "due": "2026-11-16T13:15:00",
        "unlock": "2026-11-02T13:15:00",
        "description": "<p>Complete the Writing/Balancing Reaction Equations workshop packet. This workshop covers chemical equation balancing and reaction types.</p>",
        "submission_types": "online_upload,online_text_entry",
    },
]

LAB_REPORTS = [
    {
        "id": "asgn_lab_report_1",
        "title": "Lab Report 1: Density of Solids and Significant Figures",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-09-21T13:15:00",
        "unlock": "2026-09-14T13:15:00",
        "description": "<p>Submit your lab report for Lab 1: Density of Solids and Significant Figures. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
    {
        "id": "asgn_lab_report_2",
        "title": "Lab Report 2: Conductivity of Electrolyte Solutions",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-10-05T13:15:00",
        "unlock": "2026-09-21T13:15:00",
        "description": "<p>Submit your lab report for Lab 2: Conductivity of Electrolyte Solutions. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
    {
        "id": "asgn_lab_report_3",
        "title": "Lab Report 3: Stoichiometry",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-10-12T13:15:00",
        "unlock": "2026-10-05T13:15:00",
        "description": "<p>Submit your lab report for Lab 3: Stoichiometry. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
    {
        "id": "asgn_lab_report_4",
        "title": "Lab Report 4: Acids, Bases and Buffer",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-10-19T13:15:00",
        "unlock": "2026-10-12T13:15:00",
        "description": "<p>Submit your lab report for Lab 4: Acids, Bases and Buffer. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
    {
        "id": "asgn_lab_report_5",
        "title": "Lab Report 5: Identification of Functional Groups in Organic Molecules",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-10-26T13:15:00",
        "unlock": "2026-10-19T13:15:00",
        "description": "<p>Submit your lab report for Lab 5: Identification of Functional Groups in Organic Molecules. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
    {
        "id": "asgn_lab_report_6",
        "title": "Lab Report 6: Synthesis of Aspirin",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-11-02T13:15:00",
        "unlock": "2026-10-26T13:15:00",
        "description": "<p>Submit your lab report for Lab 6: Synthesis of Aspirin. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
    {
        "id": "asgn_lab_report_7",
        "title": "Lab Report 7: Saponification",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-11-16T13:15:00",
        "unlock": "2026-11-02T13:15:00",
        "description": "<p>Submit your lab report for Lab 7: Saponification. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
    {
        "id": "asgn_lab_report_8",
        "title": "Lab Report 8: Fat From Potato Chips",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-11-23T13:15:00",
        "unlock": "2026-11-16T13:15:00",
        "description": "<p>Submit your lab report for Lab 8: Fat From Potato Chips. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
    {
        "id": "asgn_lab_report_9",
        "title": "Lab Report 9: From Starch to Sugar",
        "group": "ag_lab_reports",
        "points": 100,
        "due": "2026-11-30T13:15:00",
        "unlock": "2026-11-23T13:15:00",
        "description": "<p>Submit your lab report for Lab 9: From Starch to Sugar. Include all data tables, calculations, and analysis.</p>",
        "submission_types": "online_upload",
    },
]

QUIZZES = [
    {
        "id": "quiz_1",
        "title": "Lab Quiz 1",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-09-06T23:59:00",
        "unlock": "2026-08-31T13:15:00",
        "lock": "2026-09-06T23:59:00",
        "description": "<p>Lab Quiz 1 covering safety procedures and course orientation material. Complete by Sunday, September 6.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
    {
        "id": "quiz_2",
        "title": "Lab Quiz 2",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-09-20T23:59:00",
        "unlock": "2026-09-14T13:15:00",
        "lock": "2026-09-20T23:59:00",
        "description": "<p>Lab Quiz 2 covering Lab 1: Density of Solids and Significant Figures. Complete by Sunday, September 20.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
    {
        "id": "quiz_3",
        "title": "Lab Quiz 3",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-09-28T23:59:00",  # actually "due Sun Sep 28" which is Sep 27, but let me check... Sep 28 2026 is a Monday. The syllabus says "Due Sun, Sep 28" — let me keep it as written
        "unlock": "2026-09-21T13:15:00",
        "lock": "2026-09-28T23:59:00",
        "description": "<p>Lab Quiz 3 covering Lab 2: Conductivity of Electrolyte Solutions. Complete by Sunday, September 28.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
    {
        "id": "quiz_4",
        "title": "Lab Quiz 4",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-10-11T23:59:00",
        "unlock": "2026-10-05T13:15:00",
        "lock": "2026-10-11T23:59:00",
        "description": "<p>Lab Quiz 4 covering Lab 3: Stoichiometry. Complete by Sunday, October 11.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
    {
        "id": "quiz_5",
        "title": "Lab Quiz 5",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-10-18T23:59:00",
        "unlock": "2026-10-12T13:15:00",
        "lock": "2026-10-18T23:59:00",
        "description": "<p>Lab Quiz 5 covering Lab 4: Acids, Bases and Buffer. Complete by Sunday, October 18.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
    {
        "id": "quiz_6",
        "title": "Lab Quiz 6",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-10-25T23:59:00",
        "unlock": "2026-10-19T13:15:00",
        "lock": "2026-10-25T23:59:00",
        "description": "<p>Lab Quiz 6 covering Lab 5: Identification of Functional Groups in Organic Molecules. Complete by Sunday, October 25.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
    {
        "id": "quiz_7",
        "title": "Lab Quiz 7",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-11-01T23:59:00",
        "unlock": "2026-10-26T13:15:00",
        "lock": "2026-11-01T23:59:00",
        "description": "<p>Lab Quiz 7 covering Lab 6: Synthesis of Aspirin. Complete by Sunday, November 1.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
    {
        "id": "quiz_8",
        "title": "Lab Quiz 8",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-11-08T23:59:00",
        "unlock": "2026-11-02T13:15:00",
        "lock": "2026-11-08T23:59:00",
        "description": "<p>Lab Quiz 8 covering Lab 7: Saponification. Complete by Sunday, November 8.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
    {
        "id": "quiz_9",
        "title": "Lab Quiz 9",
        "group": "ag_quizzes",
        "points": 10,
        "due": "2026-11-29T23:59:00",
        "unlock": "2026-11-23T13:15:00",
        "lock": "2026-11-29T23:59:00",
        "description": "<p>Lab Quiz 9 covering Lab 9: From Starch to Sugar. Complete by Sunday, November 29.</p>",
        "time_limit": 30,
        "allowed_attempts": 1,
    },
]

MODULES = [
    {
        "id": "mod_week_01",
        "title": "Week 1: Safety Lecture & Course Orientation (Aug 24)",
        "position": 1,
        "unlock": "2026-08-24T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, August 24 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: Safety Lecture and Course Orientation"},
            {"type": "Assignment", "ref": "asgn_workshop_1", "title": "Workshop 1: Factor Labeling Method"},
        ],
    },
    {
        "id": "mod_week_02",
        "title": "Week 2: Independent Study - Workshop 1 (Aug 31)",
        "position": 2,
        "unlock": "2026-08-31T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, August 31 | No Lab - Independent Study"},
            {"type": "SubHeader", "title": "Complete Workshop 1 Packet independently"},
            {"type": "Quiz", "ref": "quiz_1", "title": "Lab Quiz 1"},
        ],
    },
    {
        "id": "mod_week_03",
        "title": "Week 3: No Lab - Labor Day (Sep 7)",
        "position": 3,
        "unlock": "2026-09-07T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, September 7 | No Lab - Labor Day"},
            {"type": "SubHeader", "title": "No assignments due this week"},
        ],
    },
    {
        "id": "mod_week_04",
        "title": "Week 4: LAB 1 - Density of Solids & Significant Figures (Sep 14)",
        "position": 4,
        "unlock": "2026-09-14T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, September 14 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 1 - Density of Solids and Significant Figures"},
            {"type": "Assignment", "ref": "asgn_workshop_1", "title": "Workshop 1: Factor Labeling Method (Due)"},
            {"type": "Quiz", "ref": "quiz_2", "title": "Lab Quiz 2"},
        ],
    },
    {
        "id": "mod_week_05",
        "title": "Week 5: LAB 2 - Conductivity of Electrolyte Solutions (Sep 21)",
        "position": 5,
        "unlock": "2026-09-21T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, September 21 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 2 - Conductivity of Electrolyte Solutions"},
            {"type": "Assignment", "ref": "asgn_lab_report_1", "title": "Lab Report 1: Density of Solids (Due)"},
            {"type": "Quiz", "ref": "quiz_3", "title": "Lab Quiz 3"},
        ],
    },
    {
        "id": "mod_week_06",
        "title": "Week 6: Workshop 2 - Shapes of Molecules (Sep 28)",
        "position": 6,
        "unlock": "2026-09-28T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, September 28 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: Workshop 2 - Shapes of Molecules"},
            {"type": "Assignment", "ref": "asgn_workshop_2", "title": "Workshop 2: Shapes of Molecules"},
        ],
    },
    {
        "id": "mod_week_07",
        "title": "Week 7: LAB 3 - Stoichiometry (Oct 5)",
        "position": 7,
        "unlock": "2026-10-05T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, October 5 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 3 - Stoichiometry"},
            {"type": "Assignment", "ref": "asgn_lab_report_2", "title": "Lab Report 2: Conductivity (Due)"},
            {"type": "Quiz", "ref": "quiz_4", "title": "Lab Quiz 4"},
        ],
    },
    {
        "id": "mod_week_08",
        "title": "Week 8: LAB 4 - Acids, Bases and Buffer (Oct 12)",
        "position": 8,
        "unlock": "2026-10-12T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, October 12 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 4 - Acids, Bases and Buffer"},
            {"type": "Assignment", "ref": "asgn_lab_report_3", "title": "Lab Report 3: Stoichiometry (Due)"},
            {"type": "Assignment", "ref": "asgn_workshop_2", "title": "Workshop 2: Shapes of Molecules (Due)"},
            {"type": "Quiz", "ref": "quiz_5", "title": "Lab Quiz 5"},
        ],
    },
    {
        "id": "mod_week_09",
        "title": "Week 9: LAB 5 - Functional Groups in Organic Molecules (Oct 19)",
        "position": 9,
        "unlock": "2026-10-19T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, October 19 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 5 - Identification of Functional Groups in Organic Molecules"},
            {"type": "Assignment", "ref": "asgn_lab_report_4", "title": "Lab Report 4: Acids, Bases and Buffer (Due)"},
            {"type": "Quiz", "ref": "quiz_6", "title": "Lab Quiz 6"},
        ],
    },
    {
        "id": "mod_week_10",
        "title": "Week 10: LAB 6 - Synthesis of Aspirin (Oct 26)",
        "position": 10,
        "unlock": "2026-10-26T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, October 26 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 6 - Synthesis of Aspirin"},
            {"type": "Assignment", "ref": "asgn_lab_report_5", "title": "Lab Report 5: Functional Groups (Due)"},
            {"type": "Quiz", "ref": "quiz_7", "title": "Lab Quiz 7"},
        ],
    },
    {
        "id": "mod_week_11",
        "title": "Week 11: LAB 7 - Saponification & Workshop 3 (Nov 2)",
        "position": 11,
        "unlock": "2026-11-02T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, November 2 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 7 - Saponification / Workshop 3 - Writing/Balancing Reaction Equations"},
            {"type": "Assignment", "ref": "asgn_lab_report_6", "title": "Lab Report 6: Synthesis of Aspirin (Due)"},
            {"type": "Assignment", "ref": "asgn_workshop_3", "title": "Workshop 3: Writing/Balancing Reaction Equations"},
            {"type": "Quiz", "ref": "quiz_8", "title": "Lab Quiz 8"},
        ],
    },
    {
        "id": "mod_week_12",
        "title": "Week 12: Independent Study - Workshop 3 (Nov 9)",
        "position": 12,
        "unlock": "2026-11-09T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, November 9 | No Lab - Independent Study"},
            {"type": "SubHeader", "title": "Complete Workshop 3 Packet independently"},
        ],
    },
    {
        "id": "mod_week_13",
        "title": "Week 13: LAB 8 - Fat From Potato Chips (Nov 16)",
        "position": 13,
        "unlock": "2026-11-16T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, November 16 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 8 - Fat From Potato Chips"},
            {"type": "Assignment", "ref": "asgn_lab_report_7", "title": "Lab Report 7: Saponification (Due)"},
            {"type": "Assignment", "ref": "asgn_workshop_3", "title": "Workshop 3: Writing/Balancing Reaction Equations (Due)"},
        ],
    },
    {
        "id": "mod_week_14",
        "title": "Week 14: LAB 9 - From Starch to Sugar (Nov 23)",
        "position": 14,
        "unlock": "2026-11-23T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, November 23 | 1:15 PM - 3:15 PM | Caruthers 3031"},
            {"type": "SubHeader", "title": "Topic: LAB 9 - From Starch to Sugar"},
            {"type": "Assignment", "ref": "asgn_lab_report_8", "title": "Lab Report 8: Fat From Potato Chips (Due)"},
            {"type": "Quiz", "ref": "quiz_9", "title": "Lab Quiz 9"},
        ],
    },
    {
        "id": "mod_week_15",
        "title": "Week 15: Make Up Labs (Nov 30)",
        "position": 15,
        "unlock": "2026-11-30T00:00:00",
        "items": [
            {"type": "SubHeader", "title": "Monday, November 30 | No Lab - MAKE UP LABS (Online Format)"},
            {"type": "Assignment", "ref": "asgn_lab_report_9", "title": "Lab Report 9: From Starch to Sugar (Due - Submit on Canvas)"},
        ],
    },
]


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def write_file(path, content):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def gen_course_settings():
    return """<?xml version="1.0" encoding="UTF-8"?>
<course xmlns="http://canvas.instructure.com/xsd/cccv1p0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd"
        identifier="CHM125L_Fall2026">
  <title>CHM 125L-A: Life Chemistry Laboratory - Fall 2026</title>
  <course_code>CHM 125L-A</course_code>
  <start_at>2026-08-24T00:00:00</start_at>
  <conclude_at>2026-12-11T23:59:00</conclude_at>
  <is_public>false</is_public>
  <allow_student_wiki_edits>false</allow_student_wiki_edits>
  <allow_student_forum_attachments>true</allow_student_forum_attachments>
  <default_wiki_editing_roles>teachers</default_wiki_editing_roles>
  <allow_student_organized_groups>true</allow_student_organized_groups>
  <grading_standard_enabled>true</grading_standard_enabled>
  <grading_standard_identifier_ref>gs_chm125l</grading_standard_identifier_ref>
  <group_weighting_scheme>percent</group_weighting_scheme>
</course>"""


def gen_assignment_groups():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<assignmentGroups xmlns="http://canvas.instructure.com/xsd/cccv1p0">',
    ]
    for ag in ASSIGNMENT_GROUPS:
        lines.append(f'  <assignmentGroup identifier="{ag["id"]}">')
        lines.append(f'    <title>{ag["title"]}</title>')
        lines.append(f'    <position>{ag["position"]}</position>')
        lines.append(f'    <group_weight>{ag["weight"]}</group_weight>')
        lines.append(f'  </assignmentGroup>')
    lines.append('</assignmentGroups>')
    return "\n".join(lines)


def gen_grading_standard():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<gradingStandards xmlns="http://canvas.instructure.com/xsd/cccv1p0">',
        '  <gradingStandard identifier="gs_chm125l">',
        '    <title>CHM 125L Grading Scale</title>',
        '    <data>',
    ]
    for letter, low, high in GRADING_SCALE:
        lines.append(f'      <datum>')
        lines.append(f'        <name>{letter}</name>')
        lines.append(f'        <value>{low / 100.0}</value>')
        lines.append(f'      </datum>')
    lines.append('    </data>')
    lines.append('  </gradingStandard>')
    lines.append('</gradingStandards>')
    return "\n".join(lines)


def gen_assignment_xml(asgn, position_in_group=1):
    sub_types = asgn.get("submission_types", "online_upload")
    desc = asgn.get("description", "<p>No description provided.</p>")
    unlock = ""
    if asgn.get("unlock"):
        unlock = f"\n  <unlock_at>{asgn['unlock']}</unlock_at>"
    lock = ""
    if asgn.get("lock"):
        lock = f"\n  <lock_at>{asgn['lock']}</lock_at>"

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<assignment xmlns="http://canvas.instructure.com/xsd/cccv1p0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd"
            identifier="{asgn['id']}">
  <title>{asgn['title']}</title>
  <due_at>{asgn['due']}</due_at>{unlock}{lock}
  <all_day>false</all_day>
  <assignment_group_identifierref>{asgn['group']}</assignment_group_identifierref>
  <points_possible>{asgn['points']}</points_possible>
  <grading_type>points</grading_type>
  <submission_types>{sub_types}</submission_types>
  <position>{position_in_group}</position>
  <workflow_state>published</workflow_state>
  <description>{desc}</description>
</assignment>"""


def gen_assignment_html(asgn):
    return f"""<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>{asgn['title']}</title>
</head>
<body>
  {asgn.get('description', '<p>No description provided.</p>')}
</body>
</html>"""


def gen_quiz_meta(quiz):
    lock = ""
    if quiz.get("lock"):
        lock = f"\n  <lock_at>{quiz['lock']}</lock_at>"
    unlock = ""
    if quiz.get("unlock"):
        unlock = f"\n  <unlock_at>{quiz['unlock']}</unlock_at>"

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<quiz xmlns="http://canvas.instructure.com/xsd/cccv1p0"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd"
      identifier="{quiz['id']}">
  <title>{quiz['title']}</title>
  <description>{quiz.get('description', '')}</description>
  <quiz_type>assignment</quiz_type>
  <points_possible>{quiz['points']}</points_possible>
  <due_at>{quiz['due']}</due_at>{unlock}{lock}
  <time_limit>{quiz.get('time_limit', 30)}</time_limit>
  <allowed_attempts>{quiz.get('allowed_attempts', 1)}</allowed_attempts>
  <scoring_policy>keep_highest</scoring_policy>
  <show_correct_answers>true</show_correct_answers>
  <show_correct_answers_at>{quiz['due']}</show_correct_answers_at>
  <shuffle_answers>true</shuffle_answers>
  <assignment_group_identifierref>{quiz['group']}</assignment_group_identifierref>
</quiz>"""


def gen_quiz_qti(quiz):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
  <assessment ident="{quiz['id']}" title="{quiz['title']}">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>{quiz.get('allowed_attempts', 1)}</fieldentry>
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
      <!-- Empty quiz shell - add questions in Canvas -->
    </section>
  </assessment>
</questestinterop>"""


def gen_module_meta():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<modules xmlns="http://canvas.instructure.com/xsd/cccv1p0"',
        '         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '         xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">',
    ]

    for mod in MODULES:
        lines.append(f'  <module identifier="{mod["id"]}">')
        lines.append(f'    <title>{mod["title"]}</title>')
        lines.append(f'    <position>{mod["position"]}</position>')
        if mod.get("unlock"):
            lines.append(f'    <unlock_at>{mod["unlock"]}</unlock_at>')
        lines.append(f'    <require_sequential_progress>false</require_sequential_progress>')
        lines.append(f'    <items>')

        for idx, item in enumerate(mod["items"], 1):
            item_id = f'{mod["id"]}_item_{idx}'
            lines.append(f'      <item identifier="{item_id}">')
            lines.append(f'        <title>{item["title"]}</title>')
            lines.append(f'        <position>{idx}</position>')

            if item["type"] == "SubHeader":
                lines.append(f'        <content_type>ContextModuleSubHeader</content_type>')
            elif item["type"] == "Assignment":
                lines.append(f'        <content_type>Assignment</content_type>')
                lines.append(f'        <identifierref>{item["ref"]}</identifierref>')
            elif item["type"] == "Quiz":
                lines.append(f'        <content_type>Quizzes::Quiz</content_type>')
                lines.append(f'        <identifierref>{item["ref"]}</identifierref>')

            lines.append(f'      </item>')

        lines.append(f'    </items>')
        lines.append(f'  </module>')

    lines.append('</modules>')
    return "\n".join(lines)


def gen_manifest():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<manifest identifier="CHM125L_Fall2026_manifest"',
        '          xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"',
        '          xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource"',
        '          xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest"',
        '          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '          xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lommanifest_v1p0.xsd">',
        '  <metadata>',
        '    <schema>IMS Common Cartridge</schema>',
        '    <schemaversion>1.1.0</schemaversion>',
        '    <lomimscc:lom>',
        '      <lomimscc:general>',
        '        <lomimscc:title>',
        '          <lomimscc:string language="en">CHM 125L-A: Life Chemistry Laboratory - Fall 2026</lomimscc:string>',
        '        </lomimscc:title>',
        '      </lomimscc:general>',
        '    </lomimscc:lom>',
        '  </metadata>',
        '',
        '  <organizations>',
        '    <organization identifier="org_1" structure="rooted-hierarchy">',
        '      <item identifier="root">',
    ]

    for mod in MODULES:
        lines.append(f'        <item identifier="org_{mod["id"]}">')
        lines.append(f'          <title>{mod["title"]}</title>')
        for idx, item in enumerate(mod["items"], 1):
            if item["type"] in ("Assignment", "Quiz"):
                lines.append(f'          <item identifier="org_{mod["id"]}_item_{idx}" identifierref="{item["ref"]}">')
                lines.append(f'            <title>{item["title"]}</title>')
                lines.append(f'          </item>')
        lines.append(f'        </item>')

    lines.append('      </item>')
    lines.append('    </organization>')
    lines.append('  </organizations>')
    lines.append('')
    lines.append('  <resources>')

    # Course settings
    lines.append('    <resource identifier="course_settings" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/course_settings.xml">')
    lines.append('      <file href="course_settings/course_settings.xml"/>')
    lines.append('      <file href="course_settings/assignment_groups.xml"/>')
    lines.append('      <file href="course_settings/module_meta.xml"/>')
    lines.append('      <file href="course_settings/grading_standards.xml"/>')
    lines.append('    </resource>')

    # Assignment resources
    all_assignments = WORKSHOPS + LAB_REPORTS
    for asgn in all_assignments:
        aid = asgn["id"]
        lines.append(f'    <resource identifier="{aid}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="assignments/{aid}/{aid}.html">')
        lines.append(f'      <file href="assignments/{aid}/{aid}.html"/>')
        lines.append(f'      <file href="assignments/{aid}/assignment_settings.xml"/>')
        lines.append(f'    </resource>')

    # Quiz resources
    for quiz in QUIZZES:
        qid = quiz["id"]
        lines.append(f'    <resource identifier="{qid}" type="imsqti_xmlv1p2/imscc_xmlv1p1/assessment" href="quizzes/{qid}/{qid}.xml">')
        lines.append(f'      <file href="quizzes/{qid}/{qid}.xml"/>')
        lines.append(f'      <file href="quizzes/{qid}/assessment_meta.xml"/>')
        lines.append(f'    </resource>')

    lines.append('  </resources>')
    lines.append('</manifest>')
    return "\n".join(lines)


def build():
    # Clean build dir
    import shutil
    if os.path.exists(BUILD):
        shutil.rmtree(BUILD)

    # Course settings
    write_file(os.path.join(BUILD, "course_settings", "course_settings.xml"), gen_course_settings())
    write_file(os.path.join(BUILD, "course_settings", "assignment_groups.xml"), gen_assignment_groups())
    write_file(os.path.join(BUILD, "course_settings", "grading_standards.xml"), gen_grading_standard())
    write_file(os.path.join(BUILD, "course_settings", "module_meta.xml"), gen_module_meta())

    # Assignment files (with correct position_in_group per assignment group)
    for pos, asgn in enumerate(WORKSHOPS, 1):
        aid = asgn["id"]
        write_file(os.path.join(BUILD, "assignments", aid, "assignment_settings.xml"), gen_assignment_xml(asgn, position_in_group=pos))
        write_file(os.path.join(BUILD, "assignments", aid, f"{aid}.html"), gen_assignment_html(asgn))

    for pos, asgn in enumerate(LAB_REPORTS, 1):
        aid = asgn["id"]
        write_file(os.path.join(BUILD, "assignments", aid, "assignment_settings.xml"), gen_assignment_xml(asgn, position_in_group=pos))
        write_file(os.path.join(BUILD, "assignments", aid, f"{aid}.html"), gen_assignment_html(asgn))

    # Quiz files
    for quiz in QUIZZES:
        qid = quiz["id"]
        write_file(os.path.join(BUILD, "quizzes", qid, f"{qid}.xml"), gen_quiz_qti(quiz))
        write_file(os.path.join(BUILD, "quizzes", qid, "assessment_meta.xml"), gen_quiz_meta(quiz))

    # Manifest
    write_file(os.path.join(BUILD, "imsmanifest.xml"), gen_manifest())

    # Zip into .imscc
    imscc_path = os.path.join(BASE, "CHM125L_Fall2026_Canvas_Import.imscc")
    with zipfile.ZipFile(imscc_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(BUILD):
            for fname in files:
                full = os.path.join(root, fname)
                arcname = os.path.relpath(full, BUILD)
                zf.write(full, arcname)

    print(f"Canvas import package created: {imscc_path}")
    print(f"\nPackage contents:")
    with zipfile.ZipFile(imscc_path, "r") as zf:
        for info in zf.infolist():
            print(f"  {info.filename} ({info.file_size} bytes)")

    # Clean build dir
    shutil.rmtree(BUILD)

    return imscc_path


if __name__ == "__main__":
    build()
