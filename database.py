import pymysql
from app import app
#uncomment the following line when you start project 3.2:
#from app import app


# Make sure you have data in your tables. You should have used auto increment for 
# primary keys, so all primary keys should start with 1

#you will need this helper function for all of your functions
#Use the uncommented version to test and turn in your code.  
#Comment out this version and then uncomment and use the second version below when you are importing 
#this file into your app.py in your I211_project for Project 3.2
def get_connection():
    return pymysql.connect(host="db.luddy.indiana.edu",
                           user="i211s23_rdossey",
                           password="my+sql=i211s23_rdossey",
                           database="i211s23_rdossey",
                           cursorclass=pymysql.cursors.DictCursor)

# def get_connection():
#     return pymysql.connect(host=app.config['DB_HOST'],
#                            user=app.config['DB_USER'],
#                            password=app.config['DB_PASS'],
#                            database=app.config['DB_DATABASE'],
#                            cursorclass=pymysql.cursors.DictCursor)

def get_trips():
    '''Returns a list of dictionaries representing all of the trips data'''
    sql = "select * from trip order by name"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    #add your code below, deleting the "pass"

def get_trip(trip_id):
    '''Takes a trip_id, returns a single dictionary containing the data for the trip with that id'''
    sql = "select * from trip where trip_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchone()


def add_trip(name, start_date, length, cost, location, level, leader, description):
    '''Takes as input all of the data for a trip. Inserts a new trip into the trip table'''
    sql = "insert into trip (name, start_date,length,cost,location,level,leader,description) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name, start_date, length, cost, location, level, leader, description))
        conn.commit()
        



def update_trip(trip_id, name, start_date, length, cost, location, level, leader, description):
    '''Takes a trip_id and data for a trip. Updates the trip table with new data for the trip with trip_id as it's primary key'''
    sql = "update trip set trip_id = %s, name = %s, start_date = %s, length = %s, cost = %s, location = %s, level = %s, leader = %s, description = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id , name, start_date, length, cost, location, level, leader, description))
            # Do I need brackets seperating trip_id with the rest?
        conn.commit()

def add_member(name, DoB, email, address, phone):
    '''Takes as input all of the data for a member and adds a new member to the member table'''
    sql = "insert into member (name,DoB,email,address,phone) values (%s, %s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name, DoB, email, address, phone))
        conn.commit()

    
def get_members():
    '''Returns a list of dictionaries representing all of the member data'''
    sql = "select * from members order by name"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    

def edit_member(member_id, name, DoB, email, address, phone):
    '''Given an member__id and member info, updates the data for the member with the given member_id in the member table'''
    sql = "update member set member_id = %s, name = %s, DoB = %s, email = %s, address = %s, phone = %s "
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (member_id, name, DoB, email, address, phone))
            return cursor.fetchone()
    


def delete_member(member_id):
    '''sql =" delete from member where id = %s"
    Takes a member_id and deletes the member with that member_id from the member table'''
    sql = "delete from member where member_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (member_id))
            return cursor.fetchone()
    


def add_member_trip(trip_id, member_id):
    '''Takes as input a trip_id and a member_id and inserts the appropriate data into the database that indicates the member with member_id as a primary key is attending the trip with the trip_id as a primary key'''
    sql = "insert into tripInfo (trip_ID, member_ID) values (%s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id, member_id))
        conn.commit()

    
def remove_member_trip(trip_id, member_id):
    '''Takes as input a trip_id and a member_id and deletes the data in the database that indicates that the member with member_id as a primary key 
    is attending the trip with trip_id as a primary key.'''
    sql = "delete from tripInfo (trip_ID, member_id) where id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id, member_id))
            return cursor.fetchone()

    
def get_attendees(trip_id):
    '''Takes a trip_id and returns a list of dictionaries representing all of the members attending the trip with trip_id as its primary key'''
    sql = "select * from members where memberID in (select memberID from tripInfo where tripID = %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchall()

if __name__ == '__main__':
    #add more test code here to make sure all your functions are working correctly
    try:
        print(f'All trips: {get_trips()}')
        print(f'Trip info for trip_id 1: {get_trip(1)}')
    
        # add_trip("A Day in Yellowwood", "beginner", "2023-04-22", "Yellowwood State Forest", 1, "Sy Hikist", 10, "A day of hiking in Yellowwood. Bring a water bottle" )
        # print(f'All Members: {get_members()}')
        # add_member("Tom", "Sawyer","101 E Sam Clemons Dr Bloomington, IN","tsawyer@twain.com", "812-905-1865","1970-04-01")
        # print(f"All members attending the trip with trip_id 1: {get_attendees(1)}")
        
    except Exception as e:
        print(e)