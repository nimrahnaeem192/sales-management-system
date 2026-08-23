import re
import os
import csv

class Customer:

    def __init__(self):
        self.file = "customers.csv"

# load Function
    def load_customers(self):

        customers = []

        if os.path.exists(self.file):

            with open(self.file, "r", newline="") as f:

                reader = csv.DictReader(f)

                for row in reader:
                    customers.append(row)

        else:

            with open(self.file, "w", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "CustomerID",
                    "CustomerName",
                    "CustomerPhone"
                ])

        return customers

# Save function
    def save_customers(self, customers):

        with open(self.file, "w", newline="") as f:

            fields = [
                "CustomerID",
                "CustomerName",
                "CustomerPhone"
            ]

            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            writer.writerows(customers)


# Generate id function
    def generate_id(self):

        customers = self.load_customers()

        if not customers:
            return 1

        ids = []

        for customer in customers:
            ids.append(int(customer["CustomerID"]))

        return max(ids) + 1


# Add customer function
    def add_customer(self):

        customers = self.load_customers()

        customer_id = self.generate_id()

        name = input("Enter Customer Name: ")

        while True:

            phone = input("Enter Customer Phone Number: ")

            check = re.fullmatch(r"03\d{9}", phone)

            if check:
                break

            else:
                print("Invalid Phone Number")

        customer = {

            "CustomerID": customer_id,
            "CustomerName": name,
            "CustomerPhone": phone

        }

        customers.append(customer)

        self.save_customers(customers)

        print("Customer Added Successfully")

# search customer function

    def search_customer(self):
        customers = self.load_customers()

        search_id = input("Enter Customer ID: ")

        found = False

        for customer in customers:

            if customer["CustomerID"] == search_id:
                found = True

                print(customer)

        if not found:
            print("Customer Not Found")


# update customer function

    def update_customer(self):

        customers = self.load_customers()

        update_id = input("Enter Customer ID: ")

        found = False

        for customer in customers:

            if customer["CustomerID"] == update_id:

                found = True

                customer["CustomerName"] = input("Enter New Name: ")
                customer["CustomerPhone"] = input("Enter New Phone: ")

                break

        if found:

            self.save_customers(customers)

            print("Customer Updated Successfully")

        else:

            print("Customer Not Found")


# Delte Customer function
    def delete_customer(self):

        customers = self.load_customers()

        delete_id = input("Enter Customer ID: ")

        found = False

        for customer in customers:

            if customer["CustomerID"] == delete_id:

                customers.remove(customer)

                found = True

                break

        if found:

            self.save_customers(customers)

            print("Customer Deleted Successfully")

        else:

            print("Customer Not Found")


# View Customer function
    def view_customers(self):

        customers = self.load_customers()

        if not customers:

            print("No Customers Found")

        else:

            for customer in customers:

                print(customer)