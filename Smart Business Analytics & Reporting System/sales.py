import csv
import os




        # self.sales_file = "sales.csv"

        # self.customer = Customer()
        # self.product = Product()
        # self.employee = Employee()

    # def load_sales(self):
    #
    #     sales = []
    #
    #     if os.path.exists(self.sales_file):
    #
    #         with open(self.sales_file, "r", newline="") as f:
    #
    #             reader = csv.DictReader(f)
    #
    #             for row in reader:
    #                 sales.append(row)
    #
    #     else:
    #
    #         with open(self.sales_file, "w", newline="") as f:
    #
    #             writer = csv.writer(f)
    #
    #             writer.writerow([
    #                 "SaleID",
    #                 "CustomerID",
    #                 "CustomerName",
    #                 "EmployeeID",
    #                 "EmployeeName",
    #                 "ProductID",
    #                 "ProductName",
    #                 "Month",
    #                 "Quantity",
    #                 "Price",
    #                 "Discount",
    #                 "Tax",
    #                 "Profit",
    #                 "Total"
    #             ])
    #
    #     return sales
    #
    #
    #
    # def save_sales(self, sales):
    #
    #     fields = [
    #         "SaleID",
    #         "CustomerID",
    #         "CustomerName",
    #         "EmployeeID",
    #         "EmployeeName",
    #         "ProductID",
    #         "ProductName",
    #         "Month",
    #         "Quantity",
    #         "Price",
    #         "Discount",
    #         "Tax",
    #         "Profit",
    #         "Total"
    #     ]
    #
    #     with open(self.sales_file, "w", newline="") as f:
    #
    #         writer = csv.DictWriter(f, fieldnames=fields)
    #
    #         writer.writeheader()
    #
    #         writer.writerows(sales)


    #
    #
    # def generate_sale_id(self):
    #
    #     sales = self.load_sales()
    #
    #     if not sales:
    #         return 1
    #
    #     ids = []
    #
    #     for sale in sales:
    #         ids.append(int(sale["SaleID"]))
    #
    #     return max(ids) + 1
    #
    # def add_sale(self):
    #
    #     sales = self.load_sales()
    #
    #     customers = self.customer.load_customers()
    #     products = self.product.load_products()
    #     employees = self.employee.load_employees()
    #
    #     # Check if records exist
    #     if not customers:
    #         print("No Customer Record Found")
    #         return
    #
    #     if not products:
    #         print("No Product Record Found")
    #         return
    #
    #     if not employees:
    #         print("No Employee Record Found")
    #         return
    #
    #     # ---------------- Customers ----------------
    #
    #     print("\nAvailable Customers")
    #     print("-" * 30)
    #
    #     for customer in customers:
    #         print(customer)
    #
    #     customer_id = input("Enter Customer ID: ")
    #
    #     selected_customer = None
    #
    #     for customer in customers:
    #
    #         if customer["CustomerID"] == customer_id:
    #             selected_customer = customer
    #             break
    #
    #     if selected_customer is None:
    #         print("Customer Not Found")
    #         return
    #
    #     # ---------------- Employees ----------------
    #
    #     print("\nAvailable Employees")
    #     print("-" * 30)
    #
    #     for employee in employees:
    #         print(employee)
    #
    #     employee_id = input("Enter Employee ID: ")
    #
    #     selected_employee = None
    #
    #     for employee in employees:
    #
    #         if employee["EmployeeID"] == employee_id:
    #             selected_employee = employee
    #             break
    #
    #     if selected_employee is None:
    #         print("Employee Not Found")
    #         return
    #
    #     # ---------------- Products ----------------
    #
    #     print("\nAvailable Products")
    #     print("-" * 30)
    #
    #     for product in products:
    #         print(product)
    #
    #     product_id = input("Enter Product ID: ")
    #
    #     selected_product = None
    #
    #     for product in products:
    #
    #         if product["ProductID"] == product_id:
    #             selected_product = product
    #             break
    #
    #     if selected_product is None:
    #         print("Product Not Found")
    #         return
    #
    #     # ---------------- Sale Details ----------------
    #
    #     month = input("Enter Month (Jan-Dec): ")
    #
    #     try:
    #         quantity = int(input("Enter Quantity: "))
    #     except ValueError:
    #         print("Quantity must be a number")
    #         return
    #
    #     stock = int(selected_product["Quantity"])
    #
    #     if quantity <= 0:
    #         print("Quantity must be greater than 0")
    #         return
    #
    #     if quantity > stock:
    #         print("Insufficient Stock")
    #         return
    #
    #     price = int(selected_product["Price"])
    #
    #     subtotal = quantity * price
    #
    #     discount = subtotal * 0.10
    #     tax = subtotal * 0.05
    #     profit = subtotal * 0.20
    #
    #     total = subtotal - discount + tax
    #
    #     # Update Stock
    #     selected_product["Quantity"] = str(stock - quantity)
    #
    #     self.product.save_products(products)
    #
    #     # Create Sale Record
    #     sale = {
    #
    #         "SaleID": self.generate_sale_id(),
    #
    #         "CustomerID": selected_customer["CustomerID"],
    #         "CustomerName": selected_customer["CustomerName"],
    #
    #         "EmployeeID": selected_employee["EmployeeID"],
    #         "EmployeeName": selected_employee["EmployeeName"],
    #
    #         "ProductID": selected_product["ProductID"],
    #         "ProductName": selected_product["ProductName"],
    #
    #         "Month": month,
    #
    #         "Quantity": quantity,
    #         "Price": price,
    #
    #         "Discount": discount,
    #         "Tax": tax,
    #         "Profit": profit,
    #
    #         "Total": total
    #
    #     }
    #
    #     sales.append(sale)
    #
    #     self.save_sales(sales)
    #
    #     # ---------------- Invoice ----------------
    #
    #     print("\nSale Added Successfully")
    #
    #     print("\n")
    #     print("=" * 30)
    #     print("BUSINESS INVOICE")
    #     print("=" * 30)
    #
    #     print("Sale ID       :", sale["SaleID"])
    #     print("Customer ID   :", selected_customer["CustomerID"])
    #     print("Customer Name :", selected_customer["CustomerName"])
    #
    #     print()
    #
    #     print("Employee ID   :", selected_employee["EmployeeID"])
    #     print("Employee Name :", selected_employee["EmployeeName"])
    #
    #     print()
    #
    #     print("Product ID    :", selected_product["ProductID"])
    #     print("Product Name  :", selected_product["ProductName"])
    #     print("Month         :", month)
    #
    #     print()
    #
    #     print("Quantity      :", quantity)
    #     print("Price         :", price)
    #     print("Subtotal      :", subtotal)
    #     print("Discount      :", discount)
    #     print("Tax           :", tax)
    #     print("Profit        :", profit)
    #
    #     print("-" * 30)
    #     print("Grand Total   :", total)
    #     print("=" * 30)




