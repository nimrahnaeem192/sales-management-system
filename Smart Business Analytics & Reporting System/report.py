import csv
import os


class Report:

    def __init__(self):
        self.file = "sales.csv"


    def load_sales(self):

        sales = []

        if os.path.exists(self.file):

            with open(self.file, "r", newline="") as f:

                reader = csv.DictReader(f)

                for row in reader:
                    sales.append(row)

        return sales

# Monthly Report
    def monthly_report(self):

        sales = self.load_sales()

        if not sales:
            print("No Sales Found")
            return

        monthly = {}

        for sale in sales:

            month = input("Enter Month (Jan, Feb, Mar...): ")

            break

        total = 0

        for sale in sales:

            if sale["Month"] == month:
                total += float(sale["Total"])

        print("\nMonthly Revenue")
        print("-"*30)
        print(month, ":", total)

 # Yearly Report
    def yearly_report(self):

        sales = self.load_sales()

        total = 0

        for sale in sales:

            total += float(sale["Total"])

        print("-"*30)
        print("Yearly Revenue")
        print("-"*30)
        print("Rs.", total)

  # Top Product report
    def top_products(self):

        sales = self.load_sales()

        products = {}

        for sale in sales:

            name = sale["ProductName"]
            qty = int(sale["Quantity"])

            if name in products:
                products[name] += qty
            else:
                products[name] = qty

        if not products:
            print("No Sales Found")
            return

        highest = max(products, key=products.get)

        print("Top Selling Product:", highest)
        print("Quantity Sold:", products[highest])

     # Best Customer report

    def best_customers(self):

        sales = self.load_sales()

        customers = {}

        for sale in sales:

            name = sale["CustomerName"]

            amount = float(sale["Total"])

            if name in customers:

                customers[name] += amount

            else:

                customers[name] = amount

        print("\nBest Customers")

        for customer in customers:

            print(customer, ":", customers[customer])



 # Employee Report
    def best_employees(self):

        sales = self.load_sales()

        employees = {}

        for sale in sales:

            name = sale["EmployeeName"]

            amount = float(sale["Total"])

            if name in employees:

                employees[name] += amount

            else:

                employees[name] = amount

        print("\nHighest Performing Employees")

        for employee in employees:

            print(employee, ":", employees[employee])