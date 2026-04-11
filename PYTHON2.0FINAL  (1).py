# ==========================================
#      HOTEL MANAGEMENT SYSTEM
# =========================================

# Developed By:
# 1. AKASH KUMAR
# 2. ANIKET PATRA
# 3. ADITYA KUMAR
# 4. VIGNAN
# 5. SHREE RAM
# 6. DHERYA MALHOTRA

# ------------------------------------------
# Work Distribution:
# AKASH KUMAR   -> Main Menu
# ANIKET PATRA     -> BOOK ROOM
# ADITYA KUMAR   -> Show Rooms (Display Table)
# VIGNAN         -> CHECKOUT
# SHREE RAM      -> UPDATE / REMOVE
# -----------------------------------------



print("===== HOTEL MANAGEMENT SYSTEM =====")

rooms = {}

# Create 20 rooms (101–120)
for i in range(101, 121):
    rooms[i] = {"name": "-", "mobile": "-", "id": "-", "days": 0}

# -------- NEW GLOBAL --------
room_price = 1000
total_revenue = 0

# ---------------- SHOW ROOMS ----------------
def show_rooms():
    print("\nROOM DETAILS")
    print("Room\tName\tMobile\tID\tDays")
    print("----------------------------------------")
    
    for r in rooms:
        print(f"{r}\t{rooms[r]['name']}\t{rooms[r]['mobile']}\t{rooms[r]['id']}\t{rooms[r]['days']}")
    
    input("\nPress Enter to continue...")

# ---------------- BOOK ROOM ----------------
def book_room():
    global total_revenue

    room = int(input("Enter room number: "))
    
    if room in rooms:
        if rooms[room]["name"] == "-":
            name = input("Enter name: ")

            mobile = input("Enter mobile (10 digits): ")
            if len(mobile) != 10 or not mobile.isdigit():
                print("Invalid mobile number")
                return

            id_proof = input("Enter ID: ")

            days = int(input("Enter number of days: "))
            rooms[room]["days"] = days

            total = days * room_price
            total_revenue += total

            rooms[room]["name"] = name
            rooms[room]["mobile"] = mobile
            rooms[room]["id"] = id_proof

            print("Room booked successfully")
            print("Per day fare:", room_price)
            print("Total cost:", total)

        else:
            print("Room already booked")
    else:
        print("Invalid room number")
    
    input("\nPress Enter to continue...")

# ---------------- CHECKOUT ----------------
def checkout():
    room = int(input("Enter room number: "))
    
    if room in rooms:
        if rooms[room]["name"] != "-":
            rooms[room] = {"name": "-", "mobile": "-", "id": "-", "days": 0}
            print("Checkout done")
        else:
            print("Room already empty")
    else:
        print("Invalid room")
    
    input("\nPress Enter to continue...")

# ---------------- UPDATE / REMOVE ----------------
def update_or_remove():
    room = int(input("Enter room number: "))
    
    if room in rooms and rooms[room]["name"] != "-":
        print("\n1. Update Details")
        print("2. Remove Customer")
        choice = input("Enter choice: ")

        if choice == "1":
            rooms[room]["name"] = input("Enter new name: ")
            rooms[room]["mobile"] = input("Enter new mobile: ")
            rooms[room]["id"] = input("Enter new ID: ")
            print("Details updated successfully")

        elif choice == "2":
            rooms[room] = {"name": "-", "mobile": "-", "id": "-", "days": 0}
            print("Customer removed")

        else:
            print("Invalid choice")

    else:
        print("Room empty or invalid")
    
    input("\nPress Enter to continue...")

# -------- NEW FUNCTION --------
def show_revenue():
    print("\nTotal Revenue Generated:", total_revenue)
    input("\nPress Enter to continue...")

# ---------------- DEVELOPERS ----------------
def developers():
    print("\n===== DEVELOPED BY =====")
    print("1. AKASH KUMAR")
    print("2. ANIKET PATRA")
    print("3. ADITYA KUMAR")
    print("4. VIGNAN")
    print("5. SHREE RAM")
    print("6. DHERYA MALHOTRA")
    
    input("\nPress Enter to continue...")

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Show Rooms")
        print("2. Book Room")
        print("3. Checkout")
        print("4. Update / Remove Customer")
        print("5. Exit")
        print("6. Developers")
        print("7. Total Revenue")   

        choice = input("Enter choice: ")

        if choice == "1":
            show_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            checkout()
        elif choice == "4":
            update_or_remove()
        elif choice == "5":
            print("Thank you!")
            break
        elif choice == "6":
            developers()
        elif choice == "7":
            show_revenue()
        else:
            print("Invalid choice")

# Run program
main()
