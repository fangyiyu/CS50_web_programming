class Flight:

    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)

# Create a new flight with up to 3 passengers
flight = Flight(capacity=3)
# Create a list of people
people = ["Harry", "Ron", "Hermione", "Ginny"]
# Attempt to add each person in the list to a flight
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight.")
    else:
        print(f"No available seats for {person}.")
