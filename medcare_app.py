from tkinter import *
from tkinter import messagebox

# Patient and Doctor databases
PatientDatabase = [
    {"Name": "Subhadeep Ghorai", "patient_id": "admin", "password": 1234, "age": 21, "gender": "Male"},
    {"Name": "Ravi Kumar", "patient_id": "pat001", "password": 1294, "age": 45, "gender": "Male"},
    {"Name": "Anjali Desai", "patient_id": "pat002", "password": 1134, "age": 30, "gender": "Female"},
    {"Name": "Manoj Choudhary", "patient_id": "pat003", "password": 1254, "age": 55, "gender": "Male"},
    {"Name": "Sita Reddy", "patient_id": "pat004", "password": 1294, "age": 60, "gender": "Female"},
    {"Name": "Rajesh Kapoor", "patient_id": "pat005", "password": 1034, "age": 50, "gender": "Male"}
]

DoctorDatabase = [
    {"Name": "Subhadeep Ghorai", "user_id": "admin", "password": 1234, "age": 21, "gender": "Male"},
    {"Name": "Dr. Rohan Sharma", "user_id": "rohan_sharma", "password": 1234, "specialization": "Cardiology"},
    {"Name": "Dr. Anjali Mehta", "user_id": "anjali_mehta", "password": 5678, "specialization": "Dermatology"},
    {"Name": "Dr. Vikram Singh", "user_id": "vikram_singh", "password": 9101, "specialization": "Pediatrics"},
    {"Name": "Dr. Priya Desai", "user_id": "priya_desai", "password": 1121, "specialization": "Neurology"},
    {"Name": "Dr. Arjun Patel", "user_id": "arjun_patel", "password": 3141, "specialization": "Orthopedics"}
]


class Patient:
    def PatientDashboard(self):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Patient Dashboard")

        Label(self.window, text="Welcome, Patient", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)

        def ConsultBooking():
            Doctors = [doc["Name"] for doc in DoctorDatabase]
            Times = [f"{time} PM" for time in range(1, 13)]

            selected_doctor = StringVar(value=Doctors[0])
            selected_time = StringVar(value=Times[0])

            OptionMenu(self.window, selected_doctor, *Doctors).pack(pady=5)
            OptionMenu(self.window, selected_time, *Times).pack(pady=5)

            def Report():
                with open("History.txt", "a") as file:
                    file.write(f"Consultation Booked. Doctor: {selected_doctor.get()}, Time: {selected_time.get()}\n")
                messagebox.showinfo("Confirmation", "Consultation Booked Successfully!")

            Button(self.window, text="Confirm", command=Report, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=15)

        Button(self.window, text="Book Consultation", command=ConsultBooking, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold")).pack(pady=10)
        self.window.mainloop()


class Doctor:
    def DoctorDashboard(self):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Doctor Dashboard")

        Label(self.window, text="Welcome, Doctor", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)
        self.window.mainloop()


class Admin:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Admin Panel")

        with open("History.txt", "w") as file:
            pass

        Label(self.window, text="Welcome to MedCare", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)

        roles = ["Doctor", "Patient"]
        selected_role = StringVar(value=roles[0])
        OptionMenu(self.window, selected_role, *roles).pack(pady=10)

        Label(self.window, text="Enter User ID", bg="#2F4F4F", fg="white", font=("Helvetica", 10)).pack(pady=5)
        UserID = Entry(self.window, font=("Helvetica", 10))
        UserID.pack()

        Label(self.window, text="Enter Password", bg="#2F4F4F", fg="white", font=("Helvetica", 10)).pack(pady=5)
        PassWord = Entry(self.window, show="*", font=("Helvetica", 10))
        PassWord.pack()

        def auth():
            user_id = UserID.get()
            password = PassWord.get()
            if password.isdigit():  # Ensure password is numeric
                password = int(password)

            if selected_role.get().lower() == "doctor" and self.ValidDoctor(user_id, password):
                self.window.destroy()
                Doctor().DoctorDashboard()
                '''please show the name of person who loged in into the account'''
            elif selected_role.get().lower() == "patient" and self.ValidPatient(user_id, password):
                self.window.destroy()
                Patient().PatientDashboard()
            else:
                Label(self.window, text="Authentication Failed", fg="red", bg="#2F4F4F", font=("Helvetica", 10, "bold")).pack()

        Button(self.window, text="Login", command=auth, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        self.window.mainloop()

    def ValidDoctor(self, user_id, password):
        for doctor in DoctorDatabase:
            if doctor["user_id"] == user_id and doctor["password"] == password:
                return True
        return False

    def ValidPatient(self, patient_id, password):
        for patient in PatientDatabase:
            if patient["patient_id"] == patient_id and patient["password"] == password:
                return True
        return False


# Initialize Admin Panel
admin = Admin()
