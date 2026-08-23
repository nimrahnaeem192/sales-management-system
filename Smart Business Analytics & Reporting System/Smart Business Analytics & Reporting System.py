
from customer import Customer
from product import Product
from employee import Employee
from sales import Sales
from report import Report
from analytics import Analytics
from import_export import ImportExport


customer = Customer()
product = Product()
employee = Employee()
sale = Sales()
report = Report()
analytics = Analytics()
ie = ImportExport()





# Main Function
def menu():
    while True:
        try:
            choice = int(input("1.Add Record \n 2. Search Record \n 3.Update Record \n 4.Delete Record \n 5.View Records \n 6.Reports \n 7.Analytics \n 8.Import/Export Dataset \n 9.Exit \n Enter: "))
            if choice == 1:
                while True:
                    sub = int(input("\n1.Customer \n 2.Product \n 3.Employees \n 4.Sales \n 5.Exit \n Enter: "))

                    if sub == 1:
                        customer.add_customer()

                    elif sub == 2:
                        product.add_product()

                    elif sub == 3:
                        employee.add_employee()

                    elif sub == 4:
                        sale.add_sale()

                    elif sub == 5:
                        print("Exiting....")
                        break

                    else:
                        print("Invalid Choice")


            elif choice == 2:

                while True:
                    sub = int(input("\n1.Customer \n 2.Product \n 3.Employees \n 4.Sales \n 5.Exit \n Enter:"))

                    if sub == 1:
                        customer.search_customer()

                    elif sub == 2:
                        product.search_product()

                    elif sub == 3:
                        employee.search_employee()

                    elif sub == 4:
                        sale.search_sale()

                    elif sub == 5:
                        print("Exiting.....")
                        break

                    else:
                        print("Invalid Choice")



            elif choice == 3:

                while True:
                    sub = int(input("\n1.Customer \n 2.Product \n 3.Employees \n 4.Sales \n 5.Exit \n Enter:"))

                    if sub == 1:
                        customer.update_customer()

                    elif sub == 2:
                        product.update_product()

                    elif sub == 3:
                        employee.update_employee()

                    elif sub == 4:
                        sale.update_sale()

                    elif sub == 5:
                        print("Exiting....")
                        break

                    else:
                        print("Invalid Choice")

            elif choice == 4:
                while True:
                    sub = int(input("\n1.Customer \n 2.Product \n 3.Employees \n 4.Sales \n 5.Exit \n Enter:"))

                    if sub == 1:
                        customer.delete_customer()


                    elif sub == 2:

                        product.delete_product()


                    elif sub == 3:
                        employee.delete_employee()

                    elif sub == 4:
                        sale.delete_sale()


                    elif sub == 5:
                        print("Exiting....")
                        break


                    else:
                        print("Invalid Choice")


            elif choice == 5:
                while True:
                    sub = int(input("\n1.Customer \n 2.Product \n 3.Employees \n 4.Sales \n 5.Exit \n Enter:"))

                    if sub == 1:
                        customer.view_customers()


                    elif sub == 2:
                        product.view_products()


                    elif sub == 3:
                        employee.view_employees()


                    elif sub == 4:
                        sale.view_sales()


                    elif sub == 5:
                        print("Exiting")
                        break


                    else:
                        print("Invalid Choice")

            elif choice == 6:
                while True:
                    sub = int(input("\n1.Monthly Report \n 2.Yearly Report \n 3.Top Products \n 4.Best Customers \n 5.Best Employees \n 6.Exit \n Enter: "))

                    if sub == 1:
                        report.monthly_report()


                    elif sub == 2:
                        report.yearly_report()


                    elif sub == 3:
                        report.top_products()


                    elif sub == 4:
                        report.best_customers()


                    elif sub == 5:
                        report.best_employees()


                    elif sub == 6:
                        print("Exiting")
                        break


                    else:
                        print("Invalid Choice")

            elif choice == 7:
                while True:
                    sub = int(input("\n1.View Dataset \n 2.Statistics \n 3.Highest Sale \n 4.Lowest Sale \n 5.Average Sale \n 6.Total Revenue \n 7.Sort Sales \n 8.Filter Sales \n 9.Monthly Sales \n 10.Product Sales \n 11.Clean Data \n 12.Random Sales \n 13.Exit \n Enter: "))

                    if sub == 1:
                        analytics.view_dataset()

                    elif sub == 2:
                        analytics.statistics()

                    elif sub == 3:
                        analytics.highest_sale()

                    elif sub == 4:
                        analytics.lowest_sale()

                    elif sub == 5:
                        analytics.average_sale()

                    elif sub == 6:
                        analytics.total_revenue()

                    elif sub == 7:
                        analytics.sort_sales()

                    elif sub == 8:
                        analytics.filter_sales()

                    elif sub == 9:
                        analytics.monthly_sales()

                    elif sub == 10:
                        analytics.product_sales()

                    elif sub == 11:
                        analytics.clean_data()

                    elif sub == 12:
                        analytics.random_sales()

                    elif sub == 13:
                        print("Exiting")
                        break

                    else:
                        print("Invalid Choice")


            elif choice == 8:
                while True:
                    sub = int(input("\n1.Import Dataset \n 2.Export Report \n 3.Exit \n Enter: "))
                    if sub == 1:
                        ie.import_data()

                    elif sub == 2:
                        ie.export_data()

                    elif sub == 3:
                        print("Exiting")
                        break


                    else:
                        print("Invalid Choice")


            elif choice == 9:
                print("Thank You")
                break



        except ValueError:
            print("Invalid Input")
            continue




menu()