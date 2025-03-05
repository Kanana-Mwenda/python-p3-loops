#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print (count)
        count -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    return [i ** 2 for i in int_list] 
    
def fizzbuzz():
    for i in range(1,10):
        if i%3 == 0 and i%5==0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
    pass
