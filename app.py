from flask import Flask
app = Flask(__name__)

def get_trips():
    with open(TRIPS_PATH, "r", encoding="utf-8-sig") as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        trips = []
        for i in data:
            trips.append(dict(i))

def get_members():
    with open(MEMBERS_PATH, "r", encoding="utf-8-sig") as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        members = []
        for i in data:
            members.append(dict(i))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/members")
def members():
    if os.path.isfile(MEMBERS_PATH):
        members = get_members()
    else:
        create_members_csv()
        members = get_members()
    members = get_members()
    return render_template('members.html', members=members)

@app.route("/trips")
def route():
    if os.path.isfile(TRIPS_PATH):
        trips = get_trips()
    else:
        create_members_csv()
        members = get_members()
    trips = get_trips()
    return render_template('trips.html', trips=trips)

