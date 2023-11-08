#!/usr/bin/env python3
import ipdb
import sys
import os 

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from lib.Customer import Customer
from lib.Restaurant import Restaurant
from lib.Review import Review

if __name__ == '__main__':
# WRITE YOUR TEST CODE HERE ###
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Alice", "Smith")
    customer3 = Customer("Bob", "Johnson")
    
    restaurant1 = Restaurant("The Taste of Italy")
    restaurant2 = Restaurant("Sushi Paradise")

    customer1.add_review(restaurant1, 5)
    customer2.add_review(restaurant1, 4)
    customer3.add_review(restaurant2, 4)
    
    print(customer1.full_name())  
    print(customer1.num_reviews())  
    print(Customer.find_by_name("John Doe")) 
    print(Customer.find_all_by_given_name("Alice")) 

    print(restaurant1.name)
    print(restaurant1.customers()) 
    print(restaurant1.average_star_rating()) 

    print(customer1.reviews[0].get_rating())
    print(customer1.reviews[0].get_customer().full_name()) 

# DO NOT REMOVE THIS
    ipdb.set_trace()
