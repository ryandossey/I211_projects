from flask import Flask, render_template, url_for
import csv
app = Flask(__name__)
import os

TRIP_PATH = app.root_path + '/trip_data.csv'
MEMBER_PATH = app.root_path + '/member_data.csv'
def get_trips():
    with open(TRIP_PATH, "r", encoding="utf-8-sig") as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        trips = []
        for i in data:
            trips.append(dict(i))
        return trips


def get_members():
    with open(MEMBER_PATH, "r", encoding="utf-8-sig") as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        members = []
        for i in data:
            members.append(dict(i))
        return members

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/members")
def members():
    members = get_members()
    return render_template('members.html', members=members)

@app.route("/trips")
def trips():
    trips = get_trips()
    return render_template('trips.html', trips=trips)

@app.route('/trips/<trip_id>')
def trip(trip_id=None):
    print(trip_id, type(trip_id))
    trip_id = int(trip_id)
    trips = get_trips()
    return render_template('trip.html', trip=(trips[trip_id]))

# TODO convert input type from string to int
# TODO /trips/0
# TODO error checking, what happens when the user passes /trips/lol
   
#    if dino and dino in dinosaurs.keys():
#       dinosaur = dinosaurs [dino]
#       return render_template('tripid.html', trips=trips)
#    else:
#       return render_template('index.html')

