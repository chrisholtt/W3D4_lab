from models.event import Event
import datetime

event1 = Event(datetime.datetime(2022, 5, 17), "CodeClan seminar", 100, "Edinburgh", "The impact of Flask on mental health", True)
event2 = Event(datetime.datetime(2022, 6, 13), "Israel Food convention", 5, "Edinburgh", "Come on down and enjoy some Israeli food", False)
events = [event1, event2]


def add_event_to_events(event):
    events.append(event)