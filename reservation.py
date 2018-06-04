# ///////////////////////////////////////////// #
# //   author: timesli said                  // #
# //   year  : 2018                          // #
# //   reservation.py                        // #
# //   This is the reservation class file    // #
# ///////////////////////////////////////////// #

import hotel
import customer
import notification

class Reservation():

    hotels_list = hotel.Hotel.hotels
    customers_list = customer.Customer.customers
    reservations_list = []
    room_empty_num_list = hotel.Hotel.rooms_empty_num

    def __init__(self, hotel_name, customer_name, date_in, date_out):
        if hotel_name is None or type(hotel_name) is not str:
            raise ValueError("invalid argument: hotel_name !!")
        elif customer_name is None or type(customer_name) is not str:
            raise ValueError("invalid argument: customer_name !!")
        elif date_in is None or type(date_in) is not str:
            raise ValueError('invalid argument: date_in')
        elif date_out is None or type(date_out) is not str:
            raise ValueError('invalid argument: date_out')
        self.hotel_name = hotel_name
        self.customer_name = customer_name
        self.date_in = date_in
        self.date_out = date_out

        Reservation.add_new_reservation(self, hotel_name, customer_name, date_in, date_out)

    def reserve_room(self, hotel_name):
        # loop and check if there is empty_rooms in hotel_name
        for hotel in Reservation.hotels_list:
            if hotel_name == hotel[1] and hotel[4] > 0:
                hotel[4] -= 1
                return True
        return False

    def add_new_reservation(self, hotel_name, customer_name, date_in, date_out):
        # add new reservation to reservations list
        if self.reserve_room(hotel_name):
            new_reservation = [hotel_name, customer_name, date_in, date_out]
            Reservation.reservations_list.append(new_reservation)
            room_number = self.get_room_empty_num(hotel_name, self.get_total_rooms(hotel_name))
            message = "hello " + customer_name + " your reservation at room in hotel " + hotel_name + " is confirmed from " + date_in + " to " + date_out
            print "-----------------------------------"
            print "Info confirmation"
            print "-----------------------------------"
            print "Client name   |  " + customer_name
            print "Hotel name    |  " + hotel_name
            print "Room number   |  " + str(room_number)
            print "Date in       |  " + date_in
            print "Date out      |  " + date_out
            print "-----------------------------------"
            # mobile_n = customer.Customer.customer_mobile(customer_name)
            # if mobile_n != -1:
            #     notification.Notification.send_text_message(message, mobile_n)
        else:
            print "sorry no rooms available"

    def remove_reservation(self, hotel_name, customer_name):
        # delete a booked from the reservations list
        for reserv in Reservation.reservations_list:
            if reserv[0] == hotel_name and reserv[1] == customer_name:
                return Reservation.reservations_list.remove(reserv)
        print "There is no booked with this name"

    def get_room_empty_num(self, hotel_name, total_room):
        # get reservation room number
        index = 1
        for hotel in self.room_empty_num_list:
            if hotel_name == hotel[0]:
                while index < total_room:
                    stat = False
                    for room_num in hotel:
                        if index == room_num:
                            stat = True
                    if stat:
                        index += 1
                    else:
                        hotel.append(index)
                        return index

    def get_total_rooms(self, hotel_name):
        # get total rooms in hotel
        for hotel in self.hotels_list:
            if hotel[1] == hotel_name:
                return hotel[3]
