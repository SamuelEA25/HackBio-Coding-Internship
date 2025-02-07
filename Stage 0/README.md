# Creating a Simple Script
## Objective
This task involved using the data structure of either R or Python to create a simple script to organise the names, slack usernames, emails, hobbies, countries, disciplines, and preferred programming languages of all the members in my team. This script must exclude the use of functions, loops, conditionals, and complex concepts.

Therefore, this repository contains a Python script which organises the details of team members of **Team Glycine 001** in the HacBio internship (Coding for Bio) in a systematic manner.
## Overview of the Project
The details of each team member are stored in a nested dictionary named *team_glycine_details*. Unique keys (a, b, c, d, e) are assigned to each team member easily access their details. 

The script was designed to format each member's details using f-strings to guarantee a structured presentation of the output. Numbers (1-5) were sequentially added before starting the details of all team members to order the team mates. A new line character (*\n*) was introduced after each details to introduce line breaks after each detail. 

A final print statement will print out a header showing the task stage and team name, concatenated (*+*) with the details of all the team members details in a numbering order.
## Stored Data for Each Team Member
- Name
- Slack username
- Email
- Hobby
- Country
- Discipline
- Preferred programming language
## Running the Script
Run the script by executing this command in a Python environment

`python
print team_glycine.py`        

## Output Sample

```python
HackBio Internship Stage 0 Team Glycine 001 Members

1. Name: Amaka Madubuike
   Slack username: Amaka Madubuike
   Email: amakamadubuike2023@gmail.com
   Hobby: Reading fiction and journaling
   Country: Nigeria
   Discipline: Physiology
   Preferred Programming Language: R
---
```

## Contributors
| S/N | Name                  | GitHub                        | LinkedIn                        |
|-----|-----------------------|-------------------------------|---------------------------------|
| 1   | Amaka Madubuike       |                               |                                 |
| 2   | Balamirra Yegneswaran |                               |                                 |
| 3   | Precious-Gift Alele   |                               |                                 |
| 4   | Samuel Eneojo Akor    |                               |                                 |
| 5   | Danboyi Cynthia Ihotu |                               |                                 |
