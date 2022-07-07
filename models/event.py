class Event:
    def __init__(self, _date, _name, _number_of_guests, _location, _description, _is_recurring):
        self.date = _date
        self.name = _name
        self.number_of_guests = _number_of_guests
        self.location = _location
        self.description = _description
        self.is_recurring = _is_recurring