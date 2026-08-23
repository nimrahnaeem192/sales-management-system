import pandas as pd
import numpy as np


class Analytics:

    def __init__(self):
        self.file = "sales.csv"



    def load_data(self):

        try:

            data = pd.read_csv(self.file)

            return data

        except FileNotFoundError:

            print("Sales File Not Found")

            return None


    def view_dataset(self):

        data = self.load_data()

        if data is not None:

            print(data)



    def statistics(self):

        data = self.load_data()

        if data is not None:

            print(data.describe())



    def highest_sale(self):

        data = self.load_data()

        if data is not None:

            print(data["Total"].max())



    def lowest_sale(self):

        data = self.load_data()

        if data is not None:

            print(data["Total"].min())



    def average_sale(self):

        data = self.load_data()

        if data is not None:

            print(data["Total"].mean())


    def total_revenue(self):

        data = self.load_data()

        if data is not None:

            print(data["Total"].sum())



    def sort_sales(self):

        data = self.load_data()

        if data is not None:

            sorted_data = data.sort_values("Total")

            print(sorted_data)



    def filter_sales(self):

        data = self.load_data()

        if data is not None:

            filtered = data[data["Total"] > 1000]

            print(filtered)



    def monthly_sales(self):

        data = self.load_data()

        if data is not None:

            print(data.groupby("Month")["Total"].sum())



    def product_sales(self):

        data = self.load_data()

        if data is not None:

            print(data.groupby("ProductName")["Total"].sum())



    def clean_data(self):

        data = self.load_data()

        if data is not None:

            clean = data.dropna()

            print(clean)



    def random_sales(self):

        sales = np.random.randint(100,1000,10)

        print("Random Sales")

        print(sales)

        print("Total :",np.sum(sales))

        print("Average :",np.mean(sales))

        print("Highest :",np.max(sales))

        print("Lowest :",np.min(sales))

