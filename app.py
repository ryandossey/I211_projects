from flask import Flask, render_template, url_for, request, redirect
import csv
from datetime import datetime 
app = Flask(__name__)
import os

member_fieldname = ['name', 'DoB', 'email', 'address', 'phone', 'level', 'leader', 'description']
trips_fieldname = ['name', 'start_date', 'length', 'cost', 'location', 'level', 'leader', 'description']

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
    members = get_members()
    return render_template('members.html', members=members)
        # I return the rendered template linked to members.html

@app.route("/trips")
def trips():
    # I created a new set of lists equal to the data which I read into get_trips
    trips = get_trips()
    return render_template('trips.html', trips=trips)
    # I return the rendered template linked to trips.html
    # column-sort

@app.route('/trips/<trip_id>')
def trip(trip_id=None):
    # I set the trip_id to None
    trip_id = int(trip_id)
    # I then change the input variable to be an integer
    trips = get_trips()
    # I redefine the trips variable from above
    return render_template('trip.html', trip_id=trip_id , trip=(trips[trip_id]))
    # I then create the template linking the trip_id to each trip

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
        new_members['name'] = request.form['name']
        new_members['DoB'] = request.form['DoB']
        # make sure date is valild
        # date is formated Y/M/D
        new_members['email'] = request.form['email']
        new_members['address'] = request.form['address']
        new_members['phone'] = request.form['phone']

        print(new_members)
        # append the new members to the members list
        # set the members to be members

        members.append(new_members)
        set_members(members)
        # take the user back to the members page after a sucessful completion

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
        new_trips['name'] = request.form['name']
        new_trips['location'] = request.form['location']
        new_trips['length'] = request.form['length']
        new_trips['level'] = request.form['level']
        new_trips['start_date'] = request.form['start_date']
        new_trips['cost'] = request.form['cost']
        new_trips['leader'] = request.form['leader']
        new_trips['description'] = request.form['description']


        trips.append(new_trips)
        set_trips(trips)
        # then append new trips to trips
        # and set trips to be trips

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
        new_trips['name'] = request.form['name']
        new_trips['location'] = request.form['location']
        new_trips['length'] = request.form['length']
        new_trips['level'] = request.form['level']
        new_trips['start_date'] = request.form['start_date']
        new_trips['cost'] = request.form['cost']
        new_trips['leader'] = request.form['leader']
        new_trips['description'] = request.form['description']

        trips[int(trip_id)] = new_trips
        set_trips(trips)
        # set the specific trip edited to overide the previous data in new_trips
        # set trips equal to trips


        return redirect(url_for('trips'))
        # return the user to trips
        # else: return the user to the specific trip they were on

    else:
        return render_template('trip_form.html', trip_id=trip_id, trip=(trips[trip_id]))

# @app.route('/trips/<trip_id>/delete')
