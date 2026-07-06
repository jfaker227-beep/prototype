import random

print("------------------------------------------")
print("              Welcome To H2Ops            ")
print("Cloud - Based Operations Management System")
print("------------------------------------------")

customers = []
sales = []

# =========================
# STOCK PER BRANCH
# =========================
stocks = {
    "Tagbak": 0,
    "Zarraga": 0,
    "Leganes": 0
}

# =========================
# PRICE PER BRANCH
# =========================
prices = {
    "Tagbak": 40,
    "Zarraga": 35,
    "Leganes": 45,
}

# =========================
# USER MANAGEMENT
# =========================
users = [
    {"username": "admin", "password": "1234", "role": "Admin", "branch": "Main"},
    {"username": "staff@tagbak", "password": "12345", "role": "Staff", "branch": "Tagbak"},
    {"username": "staff@zarraga", "password": "12345", "role": "Staff", "branch": "Zarraga"},
    {"username": "staff@leganes", "password": "12345", "role": "Staff", "branch": "Leganes"}
]

# =========================
# LOGIN SYSTEM
# =========================
while True:

    email = input("\nEnter Email or Username: ")
    password = input("Enter Password: ")

    current_user = None

    for user in users:

        if email == user["username"] and password == user["password"]:

            # OTP SYSTEM
            otp = random.randint(1000, 9999)
            print("\nYour OTP is:", otp)

            user_otp = input("Enter OTP: ")

            if user_otp != str(otp):
                print("\nInvalid OTP. Access Denied.")
                break

            current_user = user
            break

    if current_user is None:
        print("\nInvalid username or password.")
        continue

    role = current_user["role"]
    branch = current_user["branch"]

    print(f"\nLogin successful! Welcome {role}")

    # =========================
    # DASHBOARD
    # =========================
    while True:

        print("\n====================================")
        print(f" H2Ops DASHBOARD ({role}) ")
        print("====================================")

        print("1. View Customers")
        print("2. View Sales")
        print("3. View Stocks")

        if role == "Admin":
            print("4. Add Customer")
            print("5. Add Stock")
            print("6. Record Sale")
            print("7. User Management")
            print("8. Logout")
        else:
            print("4. Record Sale")
            print("5. Logout")

        print("====================================")

        choice = input("Enter choice: ")

        # =========================
        # VIEW CUSTOMERS
        # =========================
        if choice == "1":

            print("\n===== CUSTOMER LIST =====")

            if not customers:
                print("No customers found.")

            else:
                for i, c in enumerate(customers, start=1):

                    print(f"\nCustomer #{i}")
                    print("Name:", c["name"])
                    print("Phone:", c["phone"])
                    print("Address:", c["address"])

        # =========================
        # VIEW SALES
        # =========================
        elif choice == "2":

            print("\n===== SALES LIST =====")

            if not sales:
                print("No sales recorded.")

            else:
                for i, s in enumerate(sales, start=1):

                    print(f"\nSale #{i}")
                    print("Customer:", s["customer"])
                    print("Branch:", s["branch"])
                    print("Item:", s["item"])
                    print("Price:", s["price"])
                    print("Quantity:", s["quantity"])
                    print("Total:", s["total"])

        # =========================
        # VIEW STOCKS
        # =========================
        elif choice == "3":

            print("\n===== CURRENT STOCKS =====")

            for branch_name, stock in stocks.items():

                print("\nBranch:", branch_name)
                print("Price:", prices[branch_name])
                print("Stock:", stock)

        # =========================
        # ADD CUSTOMER
        # =========================
        elif choice == "4" and role == "Admin":

            print("\n===== ADD CUSTOMER =====")

            customers.append({
                "name": input("Enter Name: "),
                "phone": input("Enter Phone Number: "),
                "address": input("Enter Address: ")
            })

            print("\nCustomer added successfully!")

        # =========================
        # ADD STOCK
        # =========================
        elif choice == "5" and role == "Admin":

            print("\n===== ADD STOCK =====")

            print("1. Tagbak")
            print("2. Zarraga")
            print("3. Leganes")

            branch_choice = input("Select Branch: ")

            if branch_choice == "1":
                stock_branch = "Tagbak"

            elif branch_choice == "2":
                stock_branch = "Zarraga"

            elif branch_choice == "3":
                stock_branch = "Leganes"

            else:
                print("\nInvalid branch selected.")
                continue

            qty = int(input("Enter stock quantity: "))

            stocks[stock_branch] += qty

            print("\nStock added successfully!")
            print("Branch:", stock_branch)
            print("Updated Stock:", stocks[stock_branch])

        # =========================
        # ADMIN RECORD SALE
        # =========================
        elif choice == "6" and role == "Admin":

            print("\n===== RECORD SALE =====")

            customer = input("Customer Name: ")

            print("\nSelect Branch")
            print("1. Tagbak")
            print("2. Zarraga")
            print("3. Leganes")

            branch_choice = input("Enter branch number: ")

            if branch_choice == "1":
                sale_branch = "Tagbak"

            elif branch_choice == "2":
                sale_branch = "Zarraga"

            elif branch_choice == "3":
                sale_branch = "Leganes"

            else:
                print("\nInvalid branch selected.")
                continue

            item = "Mineral Water"

            price = prices[sale_branch]

            print("\nItem:", item)
            print("Price:", price)
            print("Available Stock:", stocks[sale_branch])

            quantity = int(input("Quantity: "))

            if quantity > stocks[sale_branch]:

                print("\nNot enough stock!")
                continue

            # DEDUCT STOCK
            stocks[sale_branch] -= quantity

            total = quantity * price

            sales.append({
                "customer": customer,
                "branch": sale_branch,
                "item": item,
                "price": price,
                "quantity": quantity,
                "total": total
            })

            print("\nSale recorded successfully!")
            print("Total:", total)
            print("Remaining Stock:", stocks[sale_branch])

        # =========================
        # STAFF RECORD SALE
        # =========================
        elif choice == "4" and role == "Staff":

            print("\n===== RECORD SALE =====")

            customer = input("Customer Name: ")

            item = "Mineral Water"

            price = prices[branch]

            print("\nBranch:", branch)
            print("Item:", item)
            print("Price:", price)
            print("Available Stock:", stocks[branch])

            quantity = int(input("Quantity: "))

            if quantity > stocks[branch]:

                print("\nNot enough stock!")
                continue

            # DEDUCT STOCK
            stocks[branch] -= quantity

            total = quantity * price

            sales.append({
                "customer": customer,
                "branch": branch,
                "item": item,
                "price": price,
                "quantity": quantity,
                "total": total
            })

            print("\nSale recorded successfully!")
            print("Total:", total)
            print("Remaining Stock:", stocks[branch])

        # =========================
        # USER MANAGEMENT
        # =========================
        elif choice == "7" and role == "Admin":

            print("\n===== USER MANAGEMENT =====")

            for i, user in enumerate(users, start=1):

                print(f"\nUser #{i}")
                print("Username:", user["username"])
                print("Role:", user["role"])
                print("Branch:", user["branch"])

        # =========================
        # LOGOUT
        # =========================
        elif (choice == "8" and role == "Admin") or (choice == "5" and role == "Staff"):

            print("\nLogging out...")
            break

        # =========================
        # INVALID CHOICE
        # =========================
        else:
            print("\nInvalid choice or access denied!")
