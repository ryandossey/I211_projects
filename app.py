from flask import Flask, render_template, url_for
import csv
app = Flask(__name__)
import os

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
            # I create a for loop to read in all of the data
        return members
         # I then return the newly created dictionary of the trips


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
    print(trip_id, type(trip_id))
    trip_id = int(trip_id)
    # I then change the input variable to be an integer
    trips = get_trips()
    # I redefine the trips variable from above
    return render_template('trip.html', trip=(trips[trip_id]))
    # I then create the template linking the trip_id to each trip



# TODO convert input type from string to int
# TODO /trips/0
# TODO error checking, what happens when the user passes /trips/lol
   

