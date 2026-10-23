from abc import ABC, abstractmethod


# Base class: Passenger
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


# Inheritance: Regular Passenger
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0.0


# Inheritance: Student Passenger
class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10


# Flight class
class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.__seats = seats
        self.fare = fare

    def get_available_seats(self):
        return self.__seats

    def book_seats(self, count):
        if count <= self.__seats:
            self.__seats -= count
            return True
        return False

    def display_flight(self):
        print(
            f"{self.code} | {self.airline} | "
            f"{self.source} to {self.destination} | "
            f"Seats: {self.__seats} | Fare: Rs.{self.fare}"
        )


# Booking class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.fare * tickets
        self.discount = self.subtotal * passenger.get_discount()
        self.total = self.subtotal - self.discount

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID:", self.booking_id)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger Type:", type(self.passenger).__name__)
        print("Flight Code:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Number of Tickets:", self.tickets)
        print("Base Fare per Ticket: Rs.", self.flight.fare)
        print("Subtotal: Rs.", self.subtotal)
        print("Discount:", int(self.passenger.get_discount() * 100), "%")
        print("Discount Amount: Rs.", round(self.discount, 2))
        print("Final Amount: Rs.", round(self.total, 2))
        print("=====================================")


# Main application class
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky Air", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PN303", "Air Connect", "Pune", "Hyderabad", 10, 3000)
        ]

        self.bookings = []
        self.next_booking_number = 1001

    def display_flights(self):
        print("\n========== AVAILABLE FLIGHTS ==========")
        for flight in self.flights:
            flight.display_flight()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    def book_flight(self):
        self.display_flights()

        code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Error: Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()

        if not name:
            print("Error: Passenger name cannot be blank.")
            return

        try:
            age = int(input("Enter passenger age: "))
            if age <= 0:
                print("Error: Age must be greater than zero.")
                return

            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()

            if passenger_type == "regular":
                passenger = RegularPassenger(name, age)
            elif passenger_type == "student":
                passenger = StudentPassenger(name, age)
            else:
                print("Error: Enter Regular or Student.")
                return

            tickets = int(input("Enter number of tickets: "))

            if tickets <= 0:
                print("Error: Tickets must be greater than zero.")
                return

        except ValueError:
            print("Error: Please enter a valid number.")
            return

        if tickets > flight.get_available_seats():
            print("Booking failed: Not enough seats available.")
            print("No booking was created.")
            return

        booking = Booking(
            f"BK{self.next_booking_number}",
            flight,
            passenger,
            tickets
        )

        if flight.book_seats(tickets):
            self.bookings.append(booking)
            self.next_booking_number += 1
            print("\nBooking confirmed!")
            booking.display_summary()

    def view_booking(self):
        if not self.bookings:
            print("\nNo confirmed bookings found.")
        else:
            self.bookings[-1].display_summary()

    def run(self):
        print("Welcome to Kiran Air Booking!")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3 or 4.")


# Program execution
if __name__ == "__main__":
    app = FlightBookingSystem()
    app.run()
    