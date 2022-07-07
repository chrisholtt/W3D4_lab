from flask import render_template, request, redirect
from app import app
from models.events import events, add_event_to_events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', events=events)



@app.route('/events', methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_number_of_guests = request.form["number_of_guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    event_is_recurring = request.form["is_recurring"]
    print(event_is_recurring)
    new_event = Event(event_date, event_name, event_number_of_guests, event_location, event_description, event_is_recurring)
    add_event_to_events(new_event)
    return redirect('/events')

