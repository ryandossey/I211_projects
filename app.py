from flask import Flask, render_template, url_for, request, redirect
import csv
from datetime import datetime 
app = Flask(__name__)
import os
from os.path import exists
import html

member_fieldname = ['name', 'DoB', 'email', 'address', 'phone', 'level', 'leader', 'description']
trips_fieldname = ['name', 'start_date', 'length', 'cost', 'location', 'level', 'leader', 'description']

app.config.from_pyfile(app.root_path + '/config_defaults.py')
if exists(app.root_path + '/config.py'):
    app.config.from_pyfile(app.root_path + '/config.py')
import database
# how to import database module?
# Whats the next step from here?


TRIP_PATH = app.root_path + '/trip_data.csv'
MEMBER_PATH = app.root_path + '/member_data.csv'
# These two functions set up both my members and trip paths
# I combine the app.root to the csv to create the path

def get_trips():
    with open(TRIP_PATH, "r", encoding="utf-8-sig") as csvfile:
        # I used the open csv function used in assignment 5
        data = csv.DictReader(csvfile, delimiter=",")
        trips = []
        # I then read the content of the data into a dictionary
        for i in data:
            trips.append(dict(i))
        # trips.sort(key=itemgetter("start_date"()))
        trips=sorted(trips, key=lambda dict:datetime.strptime(dict['start_date'], '%Y-%m-%d'))
# I  then sorted the trips oldest to youngest
            # I create a for loop to read in all of the data
        return trips
        # I then return the newly created dictionary of the trips


def get_members():
    with open(MEMBER_PATH, "r", encoding="utf-8-sig") as csvfile:
        # I used the open csv function used in assignment 5
        data = csv.DictReader(csvfile, delimiter=",")
        members = []
        # I then read the content of the data into a dictionary
        for i in data:
            members.append(dict(i))
        members=sorted(members, key=lambda dict:datetime.strptime(dict['DoB'], '%Y-%m-%d'))
        # I  then sorted the members oldest to youngest
            # I create a for loop to read in all of the data
        return members
         # I then return the newly created dictionary of the trips


    #  set members and trips

def set_trips(trips):
    try:
        # I refrenced the write function used in assignment 6 to help me on creating this one
        with open("trip_data.csv", "w") as csvfile:
            # I first open the csv file read in earlier
            csv_writer = csv.DictWriter(csvfile, quoting=csv.QUOTE_NONNUMERIC, fieldnames=trips_fieldname)
            csv_writer.writeheader()
            # csv.DictWriter (look it up, for the bonus problem too)
            # I create a for loop that sets the correct number read in to what is produced when written out
            # for i in range(len(trips)):
            #     csv_writer.writerow(trips[i])
            for trip in trips:
                csv_writer.writerow(trip)
    except IOError:
        print("no such file or directory")

def set_members(members):
    # I took the same steps as above writing this file
    # I refrenced the write function used in assignment 6 to help me on creating this one
    try:
        with open("member_data.csv", "w") as csvfile:
            # I first open the csv file read in earlier
            csv_writer = csv.DictWriter(csvfile, quoting=csv.QUOTE_NONNUMERIC, fieldnames=member_fieldname)
            csv_writer.writeheader()
            # I create a for loop that sets the correct number read in to what is produced when written out
            for i in range(len(members)):
                csv_writer.writerow(members[i])
    except IOError:
        print("no such file or directory")

# I create app routes for the corresponding web pages
@app.route("/")
def index():
    return render_template('index.html')
    # I created the index page and defined it
    # I return the rendered template linked to index.html

@app.route("/members")
def members():
    # I created a new set of lists equal to the data which I read into get_members
    members = database.get_members()
    # I updated my route to pull data from the database using this function
    return render_template('members.html', members=members)
        # I return the rendered template linked to members.html

@app.route("/trips")
def trips():
    # I created a new set of lists equal to the data which I read into get_trips
    trips = database.get_trips()
    # I updated my trips to pull data from the database using this function

    return render_template('trips.html', trips=trips)
    # I return the rendered template linked to trips.html
    # column-sort

@app.route('/trips/<trip_id>')
def trip(trip_id=None):
    if trip_id:
#grab trip_id from route and convert to int so we can use it as an index
        trip_id = int(trip_id)
        trips=get_trips()
        trip = trips[trip_id]
        return render_template('trip.html', trip_id=trip_id, trip=trip)
    else:
        return redirect(url_for('list_trips'))
    # # I set the trip_id to None
    # # I then change the input variable to be an integer
    # trips = database.get_trip(trip_id)
    # # I redefine the trips variable from above
    # return render_template('trip.html', trip_id=trip_id , trip=(trips[trip_id]))
    # # I then create the template linking the trip_id to each trip
    

# create a new route for members add
@app.route('/members/add', methods=['GET', 'POST'])
def add_members():
    if request.method=='POST':
        # once the request is posted
        # fill the forum with requested keys
        members = get_members()
        print(members)
        # create a new dictionary
        new_members = {}
        # fill the forum with requested keys
        name = html.escape(request.form['name'])
        DoB = html.escape(request.form['DoB'])
        # make sure date is valild
        # date is formated Y/M/D
        email = html.escape(request.form['email'])
        address = html.escape(request.form['address'])
        phone = html.escape(request.form['phone'])
        # I changed my requests to html.escape to better protect my website

        error = check_members(name, DoB, address, phone)
        if error:
            return render_template("member_form.html", error=error, name=name, DoB=DoB, address=address, phone=phone)
        # I imlimented the error checking here to make sure the data being inserted is good

        # print(new_members)
        # append the new members to the members list
        # set the members to be members

        # members.append(new_members)
        # set_members(members)
        # take the user back to the members page after a sucessful completion

        database.add_member(name, DoB, email, address, phone)
        # I then add the data inserted into the database
        return redirect(url_for('members'))
    #    if not completed, return them back to the form
    else:
        return render_template('member_form.html')


# create a new route for trips add
@app.route('/trips/add', methods=['GET', 'POST'])
def add_trips():
    if request.method=='POST':
        # make sure the request is post
        trips = get_trips()
        print(trips)
        new_trips = {}
        # create a new dictionary
        # request a set of keys
        name = html.escape(request.form['name'])
        location = html.escape(request.form['location'])
        length = html.escape(request.form['length'])
        level = html.escape(request.form['level'])
        start_date = html.escape(request.form['start_date'])
        cost = html.escape(request.form['cost'])
        leader = html.escape(request.form['leader'])
        description = html.escape(request.form['description'])
        # I changed my requests to html.escape to better protect my website



        # trips.append(new_trips)
        # set_trips(trips)
        # then append new trips to trips
        # and set trips to be trips

        database.add_trip(name, start_date, length, cost, location, level, leader, description)
        # I then add the data inserted into the database

        return redirect(url_for('trips'))
        # return the user back to trips after sucessful completion
        # else, return them back to the form

    else:
        return render_template('trip_form.html')

# create a route to allow members to edit their trips
@app.route('/trips/<trip_id>/edit', methods=['GET', 'POST'])
def edit_trip(trip_id=None):
    trips = get_trips()
    trip_id = int(trip_id)
    # set trip id = to the integer of the trip, allowing my count function to work
    if request.method=='POST':
        # post the request method
        # set up a new dictionary to store values
        # request the keys after posting
        new_trips = {}
        name = html.escape(request.form['name'])
        location = html.escape(request.form['location'])
        length = html.escape(request.form['length'])
        level = html.escape(request.form['level'])
        start_date = html.escape(request.form['start_date'])
        cost = html.escape(request.form['cost'])
        leader = html.escape(request.form['leader'])
        description= html.escape(request.form['description'])
        # I changed my requests to html.escape to better protect my website


        trips[int(trip_id)] = new_trips
        # set the specific trip edited to overide the previous data in new_trips
        # set trips equal to trips

        database.update_trip(trip_id,name, start_date, length, cost, location, level, leader, description)
        # I then update my trip data in the database
        return redirect(url_for('trips'))
        # return the user to trips
        # else: return the user to the specific trip they were on

    else:
        return render_template('trip_form.html', trip_id=trip_id, trip=(trips[trip_id]))

# @app.route('/trips/<trip_id>/delete')
# uncomment, functionality optional

# I created this function to check if the members data being inserted were good
def check_members(name, DoB, address, phone):
    error = ""
    msg=[]
    if not name:
        msg.append("Name is missing!")
    if len(name) > 15:
        msg.append("Name is too long!")
    if not DoB:
        msg.append("Date of Birth is missing!")
    if len(DoB) > 15:
        msg.append("Date of Birth is too long!")
    if not address:
        msg.append("Address is missing!")
    if len(address) > 25:
        msg.append("Address is too long!")
    if not phone:
        msg.append("Phone number is missing!")
    if len(phone) > 25:
        msg.append("Phone number is too long!")
    if len(msg)> 0:
        error= "\n".join(msg)
    return error

