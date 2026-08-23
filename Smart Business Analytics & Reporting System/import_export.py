import pandas as pd


class ImportExport:

    def import_data(self):

        file_name = input("Enter CSV File Name: ")

        try:

            data = pd.read_csv(file_name)

            print("\nDataset Imported Successfully\n")

            print(data)

        except FileNotFoundError:

            print("File Not Found")

        except Exception as e:

            print("Error:", e)



    def export_data(self):

        try:

            data = pd.read_csv("sales.csv")

            data.to_csv("Business_Report.csv", index=False)

            print("Report Exported Successfully")

        except FileNotFoundError:

            print("Sales File Not Found")

        except Exception as e:

            print("Error:", e)