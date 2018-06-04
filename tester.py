# /////////////////////////////////////// #
# //   author: timesli said            // #
# //   year  : 2018                    // #
# //   tester.py                       // #
# //   This is the tester class file   // #
# /////////////////////////////////////// #

import hotel
import reservation
import customer

class HotelTest():

    def test_add_hotel(self):
        # tester add hotel
        hotel.Hotel(20, "Rotana", "AbuDhabi", 200, 2)
        hotel.Hotel(21, "Sheraton", "AbuDhabi", 300, 1)
        hotel.Hotel(20, "Rotana", "AbuDhabi", 200, 40)

        print "========================== list hotels ==========================="
        print hotel.Hotel.hotels
        print "\n"

    def test_get_hotels_in__city(self):
        hotels = hotel.list_hotels_in_city("AbuDhabi")
        for ele in hotels:
            print ele

class CustomerTest():

    def test_add_customer(self):
        # tester add client
        customer.Customer("said", "0728782787")
        customer.Customer("tim", "07287568688")
        customer.Customer("said", "0728782787")

        print "========================= list customers ========================="
        print customer.Customer.customers
        print "\n"

class ReservationTest():
    
    def test_add_reservation(self):
        # tester add reservation
        print "======================== the reservations ========================"
        reservation.Reservation("Rotana", "said", "28/05/2018", "30/05/2018")
        reservation.Reservation("Sheraton", "said", "28/05/2018", "30/05/2018")
        reservation.Reservation("Rotana", "tim", "28/05/2018", "30/05/2018")
        reservation.Reservation("Sheraton", "said", "28/05/2018", "30/05/2018")
        print "\n"

class Tester_run():

    HotelTest().test_add_hotel()
    CustomerTest().test_add_customer()
    ReservationTest().test_add_reservation()
    HotelTest().test_get_hotels_in__city()


if __name__ == '__main__':
    Tester_run
