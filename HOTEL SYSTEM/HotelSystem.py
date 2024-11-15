import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime


class Room: 
    def __init__(self, room_number, price):
        # Encapsulation use, private attributes assigned for room number, price and is available
        self.__room_number = room_number
        self.__price = price
        self.__is_available = True

    def check_availability(self, check_in_date, check_out_date): # method that checks for the availability of the room
        return self.__is_available

    def book_room(self): ## Method to book a room if its available
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def release_room(self): #Method to release a booked room
        self.__is_available = True

    def get_price(self): #getter method to retrieve room price
        return self.__price

    def get_room_number(self):# getter method to retrieve room number
        return self.__room_number

    def get_room_type(self):
        raise NotImplementedError("This method should be implemented in child classes.")

class PremiumRoom(Room):
    def __init__(self, room_number, additional_service):
        # Inheritance and encapsulation use in passing room number and price to superclass
        super().__init__(room_number, price=200)
        # Additional attribute unique to PremiumRoom only
        self.__additional_service = additional_service

    def get_room_type(self):# Overriding get_room_type to return specific room type
        return "Premium Room"

    def get_additional_service(self):# Accessor method to retrieve additional service information
        return self.__additional_service

class SuiteRoom(Room):
    def __init__(self, room_number, amenities):
        # Inherits the attributes of the Room class with a custom price for SuiteRoom
        super().__init__(room_number, price=350)
        self.__amenities = amenities
    
    # Overriding get_room_type to specify room type as Suite Room
    def get_room_type(self):
        return "Suite Room"

    def get_amenities(self):# Accessor method to retrieve suite amenities
        return self.__amenities

class SingleRoom(Room):
    def __init__(self, room_number):
        # Inherits the attributes of the Room class with a custom price for SingleRoom
        super().__init__(room_number, price=100)

    def get_room_type(self):# Overriding get_room_type to specify room type as Suite Room
        return "Single Room"

# Payment Classes
class PaymentMethod:
    # Abstract method to be implemented by subclasses
    def pay(self, amount):
        raise NotImplementedError("This method should be implemented in child classes.")

# Concrete class for CashPayment implementing pay method
class CashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} in cash."

# Concrete class for CreditCardPayment implementing pay method
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using credit card."

# Concrete class for MobileMoneyPayment implementing pay method
class MobileMoneyPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} via mobile money."

# Reservation Class 
class Reservation:
    def __init__(self, guest_name, contact, check_in_date, check_out_date, room):
        # Attributes to store guest details and room, encapsulated within this class
        self.guest_name = guest_name
        self.contact = contact
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room = room
        self.is_checked_in = False

    def check_in(self):
        if self.room.check_availability(self.check_in_date, self.check_out_date):
            self.room.book_room()
            self.is_checked_in = True
            return True
        return False

    def check_out(self):
        if self.is_checked_in:
            self.room.release_room()
            self.is_checked_in = False
            return True
        return False

    def get_reservation_details(self):
        return {
            "Guest": self.guest_name,
            "Contact": self.contact,
            "Room Type": self.room.get_room_type(),
            "Room Number": self.room.get_room_number(),
            "Check-In": self.check_in_date,
            "Check-Out": self.check_out_date,
            "Checked In": self.is_checked_in
        }

# Hotel Class
class Hotel:
    def __init__(self, name):
        self.__name = name
        self.__rooms = []
        self.__reservations = []

    def add_room(self, room):
        self.__rooms.append(room)

    def get_available_rooms(self, check_in_date, check_out_date):
        return [room for room in self.__rooms if room.check_availability(check_in_date, check_out_date)]

    def make_reservation(self, guest_name, contact, check_in_date, check_out_date, room):
        reservation = Reservation(guest_name, contact, check_in_date, check_out_date, room)
        if reservation.check_in():
            self.__reservations.append(reservation)
            return reservation
        return None

# HotelApp GUI Application
class HotelApp:
    def __init__(self):
        self.hotel = Hotel("Grand Hotel")
        self.initialize_rooms()
        self.login_window()

    def initialize_rooms(self):
        self.hotel.add_room(SingleRoom(101))
        self.hotel.add_room(PremiumRoom(102, additional_service="Breakfast Included"))
        self.hotel.add_room(SuiteRoom(103, amenities=["Jacuzzi", "Sea View"]))
        self.hotel.add_room(PremiumRoom(201, additional_service="Spa Access"))

    def login_window(self):
        self.login_win = tk.Tk()
        self.login_win.title("Login")
        self.login_win.geometry("400x250")
        self.login_win.configure(bg="#f0f8ff")

        # Header label
        tk.Label(self.login_win, text="Hotel Reservation System", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=20)

        # Username field
        frame = tk.Frame(self.login_win, bg="#f0f8ff")
        frame.pack(pady=5)
        tk.Label(frame, text="Username:", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0, padx=10, sticky='e')
        self.username_entry = tk.Entry(frame, font=("Arial", 12))
        self.username_entry.grid(row=0, column=1)

        # Password field
        tk.Label(frame, text="Password:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, sticky='e')
        self.password_entry = tk.Entry(frame, font=("Arial", 12), show="*")
        self.password_entry.grid(row=1, column=1)

        # Login button
        tk.Button(self.login_win, text="Login", command=self.login, font=("Arial", 12), bg="#0073e6", fg="white").pack(pady=20)

        self.login_win.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "Admin1" and password == "password":
            self.login_win.destroy()
            self.main_app()
        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")

    def main_app(self):
        self.window = tk.Tk()
        self.window.title("Hotel Reservation System")
        self.window.geometry("600x700")
        self.window.configure(bg="#f0f8ff")

        # Guest Details Section
        frame_guest = tk.LabelFrame(self.window, text="Guest Details", font=("Arial", 14, "bold"), bg="#e6f0fa", padx=20, pady=20)
        frame_guest.pack(pady=10, padx=10, fill="x")

        tk.Label(frame_guest, text="Guest Name:", bg="#e6f0fa").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.guest_name_entry = tk.Entry(frame_guest, font=("Arial", 12))
        self.guest_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_guest, text="Contact Number:", bg="#e6f0fa").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.contact_entry = tk.Entry(frame_guest, font=("Arial", 12))
        self.contact_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_guest, text="Check-In Date (YYYY-MM-DD):", bg="#e6f0fa").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.check_in_date_entry = tk.Entry(frame_guest, font=("Arial", 12))
        self.check_in_date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_guest, text="Check-Out Date (YYYY-MM-DD):", bg="#e6f0fa").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.check_out_date_entry = tk.Entry(frame_guest, font=("Arial", 12))
        self.check_out_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame_guest, text="Select Room Type:", bg="#e6f0fa").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.room_type_combo = ttk.Combobox(frame_guest, values=["Single Room", "Premium Room", "Suite Room"], font=("Arial", 12))
        self.room_type_combo.set("Single Room")
        self.room_type_combo.grid(row=4, column=1, padx=10, pady=5)

        # Reservation Controls Section
        frame_controls = tk.Frame(self.window, bg="#f0f8ff")
        frame_controls.pack(pady=10)

        tk.Button(frame_controls, text="Make Reservation", command=self.make_reservation, font=("Arial", 12), bg="#0073e6", fg="white").grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame_controls, text="Show Available Rooms", command=self.show_available_rooms, font=("Arial", 12), bg="#0073e6", fg="white").grid(row=0, column=1, padx=10, pady=5)
        tk.Button(frame_controls, text="Check In", command=self.check_in_guest, font=("Arial", 12), bg="#0073e6", fg="white").grid(row=1, column=0, padx=10, pady=5)
        tk.Button(frame_controls, text="Check Out", command=self.check_out_guest, font=("Arial", 12), bg="#0073e6", fg="white").grid(row=1, column=1, padx=10, pady=5)
        tk.Button(frame_controls, text="Make Payment", command=self.make_payment, font=("Arial", 12), bg="#0073e6", fg="white").grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.window.mainloop()

    def show_available_rooms(self):
        check_in_date = self.check_in_date_entry.get()
        check_out_date = self.check_out_date_entry.get()

        # Date validation
        try:
            check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")
            if check_out_date <= check_in_date:
                raise ValueError("Check-out date must be after check-in date.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid date format or range. {e}")
            return

        available_rooms = self.hotel.get_available_rooms(check_in_date, check_out_date)
        if not available_rooms:
            messagebox.showinfo("Available Rooms", "No rooms are available for the selected dates.")
            return

        room_list = [f"{room.get_room_type()} - Room {room.get_room_number()} - ${room.get_price()}" for room in available_rooms]
        messagebox.showinfo("Available Rooms", "\n".join(room_list))

    def make_reservation(self):
        guest_name = self.guest_name_entry.get()
        contact = self.contact_entry.get()
        check_in_date = self.check_in_date_entry.get()
        check_out_date = self.check_out_date_entry.get()
        room_type = self.room_type_combo.get()

        # Validate input fields
        if not guest_name or not contact or not check_in_date or not check_out_date:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")
            if check_out_date <= check_in_date:
                raise ValueError("Check-out date must be after check-in date.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid date format or range. {e}")
            return

        available_rooms = self.hotel.get_available_rooms(check_in_date, check_out_date)
        if not available_rooms:
            messagebox.showinfo("Error", "No rooms are available for the selected dates.")
            return

        # Match room type with the room selected by the guest
        room = None
        for available_room in available_rooms:
            if available_room.get_room_type() == room_type:
                room = available_room
                break

        if room:
            reservation = self.hotel.make_reservation(guest_name, contact, check_in_date, check_out_date, room)
            if reservation:
                messagebox.showinfo("Reservation Success", f"Reservation made for {guest_name} in Room {room.get_room_number()}.")
            else:
                messagebox.showerror("Error", "Reservation failed.")
        else:
            messagebox.showerror("Error", "Selected room type is not available.")

    def check_in_guest(self):
        guest_name = self.guest_name_entry.get()
        for reservation in self.hotel._Hotel__reservations:
            if reservation.guest_name == guest_name and not reservation.is_checked_in:
                reservation.check_in()
                messagebox.showinfo("Check-In", f"Checked in {guest_name} to Room {reservation.room.get_room_number()}.")
                return
        messagebox.showerror("Error", "Guest not found or already checked in.")

    def check_out_guest(self):
        guest_name = self.guest_name_entry.get()
        for reservation in self.hotel._Hotel__reservations:
            if reservation.guest_name == guest_name and reservation.is_checked_in:
                reservation.check_out()
                messagebox.showinfo("Check-Out", f"Checked out {guest_name} from Room {reservation.room.get_room_number()}.")
                return
        messagebox.showerror("Error", "Guest not found or not checked in.")

    def make_payment(self):
        guest_name = self.guest_name_entry.get()
        
        # Find the reservation for the guest
        for reservation in self.hotel._Hotel__reservations:
            if reservation.guest_name == guest_name and reservation.is_checked_in:
                room_price = reservation.room.get_price()

                # Prompt the user with the payment methods in a combo box
                payment_method_window = tk.Toplevel(self.window)
                payment_method_window.title("Select Payment Method")
                payment_method_window.geometry("300x150")

                tk.Label(payment_method_window, text=f"Room Price: ${room_price}", font=("Arial", 14)).pack(pady=20)

                payment_method_label = tk.Label(payment_method_window, text="Select Payment Method:", font=("Arial", 12))
                payment_method_label.pack(pady=5)

                payment_method_combo = ttk.Combobox(payment_method_window, values=["Cash", "Credit Card", "Mobile Money"])
                payment_method_combo.set("Cash")  # Default option
                payment_method_combo.pack(pady=10)

                # Define the function to handle payment
                def process_payment():
                    selected_method = payment_method_combo.get()
                    payment = None

                    if selected_method == 'Cash':
                        payment = CashPayment()
                    elif selected_method == 'Credit Card':
                        payment = CreditCardPayment()
                    elif selected_method == 'Mobile Money':
                        payment = MobileMoneyPayment()

                    if payment:
                        payment_result = payment.pay(room_price)
                        messagebox.showinfo("Payment Success", payment_result)
                        payment_method_window.destroy()
                    else:
                        messagebox.showerror("Error", "Invalid payment method selected.")

                # Button to confirm payment method
                confirm_button = tk.Button(payment_method_window, text="Confirm Payment", command=process_payment)
                confirm_button.pack(pady=20)

                payment_method_window.mainloop()
                return
        
        # If no active reservation is found for this guest
        messagebox.showerror("Error", "No active reservation found for this guest.")

# Run the application
if __name__ == "__main__":
    HotelApp()
