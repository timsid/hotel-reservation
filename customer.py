# /////////////////////////////////////////// #
# //   author: timesli said                // #
# //   year  : 2018                        // #
# //   customer.py                         // #
# //   This is the customer class file     // #
# /////////////////////////////////////////// #

class Customer():

    customers = []

    def __init__(self, customer_name, mobile_n):
        if customer_name is None or type(customer_name) is not str:
            raise ValueError("invalid argument: customer_name !!")
        elif mobile_n is None or type(mobile_n) is not str:
            raise ValueError("invalid argument: mobile_n !!")
        self.customer_name = customer_name
        self.mobile_n = mobile_n

        self.add_customer_to_list(customer_name, mobile_n)

    def is_customer_exist(self, customer_name, mobile_n):
        # check if there customer exist or no
        for client in self.customers:
            if client[0] == customer_name and client[1] == mobile_n:
                return True
        return False

    def add_customer_to_list(self, customer_name, mobile_n):
        # add customer in a customer list
        if self.is_customer_exist(customer_name, mobile_n):
            print "this customer is exist !!"
        else:
            self.customers.append([customer_name, mobile_n])

    def remove_customer(self, customer_name, mobile_n):
        # delete a customer info in the list
        for client in self.customers:
            if client[0] == customer_name and client[1] == mobile_n:
                print "this customer is removed in the list customers"
                return self.customers.remove(client)
        print "this customer is not in customers list"

    def customer_mobile(self, customer_name):
        # get a customer mobile number
        for client in Customer.customers:
            if client[0] == customer_name:
                return client[1]
        return -1
