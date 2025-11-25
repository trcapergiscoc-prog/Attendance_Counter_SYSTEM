# Attendance Counter System

def login_system(): 
    print("===== WELCOME TO ATTENDANCE COUNTER SYSTEM =====")
    print("[1] Log In")
    print("[2] Exit")

    while True:
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            under_statement()
            break
        elif choice == "2":
            print("System Ended. Goodbye!")
            exit()
        else:
            print("Invalid input. Please choose 1 or 2 only.")


def under_statement():
    print("\n--- UNDER STATEMENT ---")
    print("This system is only for authorized users.")

    while True:
        password = input("Enter password to proceed: ")

        if password == "16289306":
            print("Password correct. Proceeding to Main Menu...\n")
            main_menu()
            break
        else:
            print("Incorrect password. Try again or type 'exit' to go back.")
            retry = input("Do you want to try again? (yes/no): ").lower()

            if retry == "no":
                print("Returning to Under Statement...\n")
                continue


def main_menu():
    while True:
        print("===== MAIN MENU =====")
        print("[1] View Student List")
        print("[2] Go Back to Log In")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_student_list()
            break
        elif choice == "2":
            print("Returning to Log In...\n")
            login_system()
            break
        else:
            print("Invalid input. Please choose 1 or 2 only.\n")


def view_student_list():
    print("\n--- STUDENT LIST ---")
    
    students = [
        "John Cruz", "Maria Santos", "Liza Reyes", "Mark Dela Cruz",
        "Anne Lopez", "James Tan", "Sophia Garcia", "Luke Mendoza",
        "Ella Ramos", "Noah Villanueva"
    ]

    date = input("Enter date (MM/DD/YYYY): ")
    print(f"\nAttendance Checking for Date: {date}")
    print("Enter 'P' for Present or 'A' for Absent.\n")

    present_count = 0

    for i, student in enumerate(students, start=1):
        while True:
            status = input(f"{i}. {student}: ").upper()

            if status == 'P':
                present_count += 1
                print("Student is present.")
                break
            elif status == 'A':
                print("Student is absent.")
                break
            else:
                print("Invalid input! Please enter 'P' or 'A' only.\n")

    total_students = len(students)
    attendance_percentage = (present_count / total_students) * 100

    print("\n===== ATTENDANCE SUMMARY =====")
    print(f"Date: {date}")
    print(f"Total Students: {total_students}")
    print(f"Present: {present_count}")
    print(f"Absent: {total_students - present_count}")
    print(f"Attendance Percentage: {attendance_percentage:.2f}%")

    print("\nSystem Ended. Thank you for using Attendance Counter System!")


# Start the program
login_system()