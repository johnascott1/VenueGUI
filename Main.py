from peewee import *
import PyQt5
import datetime


from PyQt5 import QtWidgets

from VenuePyqt5 import UI_MainWindow  # importing our generated file

import sys


class mywindow(QtWidgets.QMainWindow):


def __init__(self):
    super(mywindow, self).__init__()

    self.ui = Ui_MainWindow()

    self.ui.setupUi(self)


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())

# specify product name
# specify quanitity sold

db = SqliteDatabase('vendor_management.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


# class VendorItems(BaseModel):
#   item_name = CharField()

#  def __str__(self):
#      return f'Item: {self.item_name}'

class Show(BaseModel):
    show_venue = CharField()
    show_city = CharField()
    show_state = CharField()
    show_date = DateField()
    posters_sold = IntegerField()
    CDs_sold = IntegerField()
    tshirts_sold = IntegerField()

    def __str__(self):
        return f'Venue: {self.show_venue}   City: {self.show_city}  State: {self.show_state}    Date: {self.show_date}'


# class Sales(Model):
#   show_venue = CharField()
#  posters_sold = IntegerField()
# CDs_sold = IntegerField()
# tshirts_sold = IntegerField()


db.connect()
db.create_tables([Show])


# db.create_tables([Show])
def main():
    while True:

        print("1) Add Venue")
        print("2) Show All Venues")
        print("3) Exit")

        selection = input("Please Select:")
        if selection == '1':
            addVenue()
        elif selection == '2':
            showAllVenues()
        elif selection == '3':
            break
        else:
            print("Unknown Option Selected!")


def addVenue():
    enterVenue = input("Enter the name of the show: ")
    enterCity = input("Enter the name of the city: ")
    enterState = input("Enter the name of the state: ")
    enterDate = input("Enter the date of the show: ")
    enterPoster = int(input("Enter the number of posters sold: "))
    enterCD = int(input("Enter the number of CDs sold: "))
    enterTshirt = int(input("Enter the number of T-Shirts sold: "))
    show = Show(show_venue=enterVenue)
    show.save()


def showAllVenues():
    # allItems = VendorItems.select()
    # for item in allItems:
    # print(item)
    print(0)


main()