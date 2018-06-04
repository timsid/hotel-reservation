# /////////////////////////////////////// #
# //   author: timesli said            // #
# //   year  : 2018                    // #
# //   hotel.py                        // #
# //   This is the hotel class file    // #
# /////////////////////////////////////// #

class Hotel():

    hotels = []
    rooms_empty_num = []

    def __init__(self, number, hotel_name, city, total_rooms, empty_rooms):
        if number < 0 or type(number) is str:
            raise ValueError("invalid argument: number !!")
        if hotel_name is None or type(hotel_name) is int:
            raise ValueError("invalid argument: hotel_name !!")
        if city is None or type(city) is not str:
            raise ValueError("invalid argument: city !!")
        if total_rooms is None or type(total_rooms) is not int:
            raise ValueError("invalid argument: total_rooms !!")
        if empty_rooms is None or type(empty_rooms) is not int:
            raise ValueError("invalid argument: empty_rooms !!")
        self.number = number
        self.hotel_name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

        self.add_hotel_in_list(number, hotel_name, city, total_rooms, empty_rooms)

    def is_hotel_exist(self, hotel_name, city):
        # check if there hotel exist or no
        for hotel in Hotel.hotels:
            if hotel[1] == hotel_name and hotel[2] == city:
                return True
            return False

    def add_hotel_in_list(self, number, hotel_name, city, total_rooms, empty_rooms):
        # add a new hotel to hotels list
        if self.is_hotel_exist(hotel_name, city):
            print "Hotel " + hotel_name + " in the city " + city + " is exist"
        else:
            Hotel.hotels.append([number, hotel_name, city, total_rooms, empty_rooms])
            self.rooms_empty_num.append([hotel_name])

    def remove_hotel(self, hotel_name, city):
        # delete a hotel from the list
        for hotel in Hotel.hotels:
            if hotel[1] == hotel_name and hotel[2] == city:
                Hotel.hotels.remove(hotel)

def list_hotels_in_city(city):
    # get list hotels in a city
    hotels_list = []
    print "================= list hotels in a " + city + " city ================="
    for hotel in Hotel.hotels:
        if hotel[2] == city:
            hotels_list.append(hotel[1])
    return hotels_list
