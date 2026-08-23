import csv
import os

class Product:

    def __init__(self):
        self.file = "products.csv"


    def load_products(self):

        products = []

        if os.path.exists(self.file):

            with open(self.file, "r", newline="") as f:

                reader = csv.DictReader(f)

                for row in reader:
                    products.append(row)

        else:

            with open(self.file, "w", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "ProductID",
                    "ProductName",
                    "Category",
                    "Price",
                    "Quantity",
                    "Supplier"
                ])

        return products



    def save_products(self, products):

        with open(self.file, "w", newline="") as f:

            fields = [
                "ProductID",
                "ProductName",
                "Category",
                "Price",
                "Quantity",
                "Supplier"
            ]

            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            writer.writerows(products)


    def generate_id(self):

        products = self.load_products()

        if not products:
            return 101

        ids = []

        for product in products:
            ids.append(int(product["ProductID"]))

        return max(ids) + 1



    def add_product(self):

        products = self.load_products()

        product = {

            "ProductID": self.generate_id(),
            "ProductName": input("Enter Product Name: "),
            "Category": input("Enter Category: "),
            "Price": int(input("Enter Product Price: ")),
            "Quantity": int(input("Enter Quantity: ")),
            "Supplier": input("Enter Supplier Name: ")

        }

        products.append(product)

        self.save_products(products)

        print("Product Added Successfully")



    def search_product(self):

        products = self.load_products()

        search_id = input("Enter Product ID: ")

        found = False

        for product in products:

            if product["ProductID"] == search_id:

                found = True

                print(product)

        if not found:

            print("Product Not Found")




    def update_product(self):

        products = self.load_products()

        update_id = input("Enter Product ID: ")

        found = False

        for product in products:

            if product["ProductID"] == update_id:

                found = True

                product["ProductName"] = input("Enter New Name: ")
                product["Category"] = input("Enter New Category: ")
                product["Price"] = int(input("Enter New Price: "))
                product["Quantity"] = int(input("Enter New Quantity: "))
                product["Supplier"] = input("Enter New Supplier: ")

                break

        if found:

            self.save_products(products)

            print("Product Updated Successfully")

        else:

            print("Product Not Found")


    def delete_product(self):

        products = self.load_products()

        delete_id = input("Enter Product ID: ")

        found = False

        for product in products:

            if product["ProductID"] == delete_id:

                products.remove(product)

                found = True

                break

        if found:

            self.save_products(products)

            print("Product Deleted Successfully")

        else:

            print("Product Not Found")



    def view_products(self):

        products = self.load_products()

        if not products:

            print("No Products Found")

        else:

            for product in products:

                print(product)