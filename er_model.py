import sqlite3

connection = sqlite3.connect("hstu.db")
cursor = connection.cursor()

# create user table query
table_user = """
    CREATE TABLE user(
    user_id int NOT NULL,
    username varchar(30) NOT NULL,
    user_type varchar(30),
    PRIMARY KEY(user_id));
"""

# create role table query
table_role = """
    CREATE TABLE role(
    role_id int NOT NULL,
    user_id int  REFERENCES user(user_id),
    responsibility varchar(30),    
    PRIMARY KEY(role_id));
"""

# create club table unfinished
table_club= """
    CREATE TABLE club(
    club_id int NOT NULL,
    club_name varchar(30) NOT NULL,
    president_name varchar(30),
    president_id int  ,   
    PRIMARY KEY(club_id));    
"""


# create events table
table_event = """
    CREATE TABLE event(
    eid int NOT NULL,
    club_name varchar(30) NOT NULL,
    president_name varchar(30),
    president_id int,     
    PRIMARY KEY(eid));    
"""
# # create responsibilities table
# table_responsibilities = """
#     CREATE TABLE responsibility(
#     eid int NOT NULL
# """

try:
    cursor.execute(table_user)
    cursor.execute(table_role)
    cursor.execute(table_club)
    cursor.execute(table_event)
    # cursor.execute(table_responsibilities)

except:
    print('Something Wrong in your query')