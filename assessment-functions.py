from __future__ import division

# The future division statement, spelled "from __future__ import
# division", will change the / operator to mean true division
# throughout the module.

"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

town = ['Taipei', 'San Francisco']
def is_town_name(hometown):
    """Will determine if town is my hometown."""
    if hometown in town:
    #iterates thgouth town list to see if hometown is in the town list
        return True
    else:
        return False

print is_town_name('Taipei')

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def full_name(first, last):
    """Will return the full name of an individual"""
    return first + " " + last
    #concatenates first and last name

print full_name('Lydia','Huang')

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def from_same_town(hometown, first, last):
    """Will determine if I have the same hometown as another person."""
    name = first + " " + last
    if is_town_name(hometown):
    #pass in the is_town_name function
        return "Hi, " + name + ", we're from the same place!" 
    else:
        return "Hi, " + name + ", where are you from?"
    #if new hometown is same to my hometown return first statement, otherwise,
    #return last statement

print from_same_town('Bali', 'Tom', 'Adams')
###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."

berry = ["strawberry","cheery","blackberry"]
def is_berry(fruit):
    """Determines if fruit is a berry"""
    if fruit in berry:
    #iterates through berry list to see if fruit is inside
        return True
    else:
        return False

print is_berry("blackberry")
print is_berry("durian")

# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""
    if is_berry(fruit):
    #passes in is_berry function, if fruit is in the berry list
        return 0
    else:
        return 5

print shipping_cost("blackberry")
print shipping_cost("durian")
     


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""
    lst.append(num)
    #adds the number to the list
    return lst

print append_to_list([3, 5, 7], 2)
  


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.



def calculate_price(base_price, state, tax=5): 
#takes in 3 parameters but kept failing
#when I passed in the given, finally figured out how to pass in the default tax of 5% 
#looked up from __future__ import division somewhere on stack overflow
"""Will return the total cost of an item depending on what state the purchase is done at."""


    tax = tax/100  
    #turns the input into 2 decimals ex. 2% = 0.02
    total_cost = base_price + (base_price*tax)

    if state == 'CA':
        return total_cost + (total_cost * 0.03)
    #adds a 3% recycling fee to the total cost if in California

    elif state == 'PA':
        return total_cost + 2.00
    #adds a $2 highway safety fee to the total cost 

    elif state == 'MA':
        if base_price < 100.00:
            return total_cost + 1.00 
        else: 
            return total_cost + 3.00
    #adds a commonwealth fund fee of $1 to the total cost if the price is under $100, 
    #if price is  over $100, add $3 to the total coast 

    return total_cost 

print calculate_price(40, "CA")
print calculate_price(400, "NM")
print calculate_price(150, "OR", 0.0)
print calculate_price(60, "PA")
print calculate_price(38, "MA")
print calculate_price(126, "MA")

    

###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
