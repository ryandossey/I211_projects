from flask import Flask, render_template, url_for, request, redirect
import csv
from datetime import datetime 
app = Flask(__name__)
import os

member_fieldname = ['name', 'DoB', 'email', 'address', 'phone', 'level', 'leader', 'description']
trips_fieldname = ['name', 'start_date', 'length', 'cost', 'location', 'level', 'leader', 'description', 'ID']

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
            csv_writer.writeheader
            # csv.DictWriter (look it up, for the bonus problem too)
            # I create a for loop that sets the correct number read in to what is produced when written out
            for i in range(len(trips)):
                csv_writer.writerow(trips[i])
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
    print(trip_id, type(trip_id))
    trip_id = int(trip_id)
    # I then change the input variable to be an integer
    trips = get_trips()
    # I redefine the trips variable from above
    return render_template('trip.html', trip_id=trip_id , trip=(trips[trip_id]))
    # I then create the template linking the trip_id to each trip

    # # I set the trip_id to None
    # trips = get_trips()
    # trip = trips[int(trip_id)]
    # # I then change the input variable to be an integer
    # # I redefine the trips variable from above
    # return render_template('trip.html', trip=trip)
    # I then create the template linking the trip_id to each trip


@app.route('/members/add', methods=['GET', 'POST'])
def add_members():
    if request.method=='POST':
        members = get_members()
        print(members)
        # change members to members_list
        new_members = {}
        new_members['name'] = request.form['name']
        new_members['DoB'] = request.form['DoB']
        # make sure date is valild
        # date is formated Y/M/D
        new_members['email'] = request.form['email']
        new_members['address'] = request.form['address']
        new_members['phone'] = request.form['phone']

        print(new_members)

        members.append(new_members)
        set_members(members)

        return redirect(url_for('members'))
       
    else:
        return render_template('member_form.html')

        # variable and function both named members


@app.route('/trips/add', methods=['GET', 'POST'])
def add_trips():
    if request.method=='POST':
        trips = get_trips()
        print(trips)
        # count = len(trips) +1
        new_trips = {}
        new_trips['name'] = request.form['name']
        new_trips['location'] = request.form['location']
        new_trips['length'] = request.form['length']
        new_trips['level'] = request.form['level']
        new_trips['start_date'] = request.form['start_date']
        new_trips['cost'] = request.form['cost']
        new_trips['leader'] = request.form['leader']
        new_trips['description'] = request.form['description']
        # new_trips['ID'] = count

        trips.append(new_trips)
        set_trips(trips)

        return redirect(url_for('trips'))

    else:
        return render_template('trip_form.html')


@app.route('/trips/<trip_id>/edit', methods=['GET', 'POST'])
def edit_trip(trip_id=None):
    trip_id = int(trip_id)
    trips = get_trips()

    if request.method=='POST':
        # questions for hours
        # would I use a get function? (becaue I need to pull data and then edit it)
        # how would i impliment that compared to what i have now
        new_trips = {}
        new_trips['name'] = request.form['name']
        new_trips['location'] = request.form['location']
        new_trips['length'] = request.form['length']
        new_trips['level'] = request.form['level']
        new_trips['start_date'] = request.form['start_date']
        new_trips['cost'] = request.form['cost']
        new_trips['leader'] = request.form['leader']
        new_trips['description'] = request.form['description']

# append will duplicate data, i want to replace the value at index
        trips.insert(new_trips)
        # would it be an insert?
        set_trips(trips)

        return redirect(url_for('trips'))

    else:
        request.method=='GET'
        return render_template('trip_form.html', trip=(trips[trip_id]))

# @app.route('/trips/<trip_id>/delete')
