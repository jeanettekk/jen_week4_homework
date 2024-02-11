# imports the random module
import random

# Jen Section
# Created a list with 3 items and stored in it in the cheese variable
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

print('QUESTION 1\n')
# Adding Oke in this way adds each character into the list
# cheese += 'Oke'

# Square brackets MUST be included to add the whole word as one item in the list
cheese += ['Oke', 'Mozarella']

# Prints the new list with the additional two items
print('Added two items to cheese list:\n',cheese, '\n', '-' * 100, '\nQUESTION 2\n')

# A string is assigned to the variable, tup
tup = 'Hello'

# length function returns how many characters are in the string, then it's printed
print(f'How many characters in the string: {len(tup)}')

# The tup variable is re-assigned a new value, a tuple with one item
tup = 'Hello',
# How many items are in the tuple is returned by the length function and printed
print(f'How many items are in the tuple: {len(tup)}')

print('\n','-' * 100,'\nQUESTION 3 - Lottery\n')

# Stored an empty set to random_numbers variable
random_numbers = set()

# length function checks how many items are in the set, random_numbers,
# while loops runs only while the number of the items in the set are NOT equal to 6
while not len(random_numbers) == 6:

    # random is a module, not an object
    # Therefore, randint() is a function even if it's starting with a dot
    # randint function returns a random integer between 1-50
    # add method adds the random number to the set, random_numbers, only unique numbers are saved
    random_numbers.add(random.randint(1, 50))

# tuple method constructs a tuple from the random_numbers set
# As a tuple, the order of items will now remain the same
numbers_tuple = tuple(random_numbers)

# enumerate function returns the index and value of each item in numbers_tuple
# for loop will iterate through each item
for index_tuple, value_tuple in enumerate(numbers_tuple):

    # if the index is equal to 0, the first item's index, execute this code
    if index_tuple == 0:

        # prints a string announcing the lottery numbers and the value of the first item
        # end= adds a space at the end of the string
        print(f'Lottery Numbers: {value_tuple}', end=' ')

    # if the index is NOT equal to 0, execute this code
    else:
        # prints the rest of the values in the tuple with a space after each one
        print(value_tuple, end=' ')

# map function applies a given function, the string function, to each item of numbers_tuple
# string function converted the lottery numbers into strings
# join method concatenates the strings with a space in between each number
# the string is assigned to the file_numbers variable
file_numbers = ' '.join(map(str, numbers_tuple))

# with statement properly manages resources, automatically closing the file after this block of code is executed
# open function opens the file lottery_history.txt in 'append' mode as the variable, file
with open('lottery_history.txt', 'a') as file:

    # write method adds the string from file_numbers variable and a new line onto lottery_history.txt
    file.write(f'{file_numbers}\n')

    # A string is printed to inform the user that the lottery numbers have been saved
    print('\nSaved in lottery_history.txt\n')

# an empty dictionary is assigned to number_frequency variable
number_frequency = {}

# with statement properly manages resources, automatically closing the file after this block of code is executed
# open function opens the file lottery_history.txt in 'append' mode as the variable, file
with open('lottery_history.txt', 'r') as file:

    # for loop iterates over each line in lottery_history.txt and assigns it to the variable, line
    for line in file:

        # strip() removes the leading and trailing whitespaces of each string
        # split() turns each line into a list. By default, it will divide each item by the spaces
        # The list is stored in numbers_history variable
        numbers_history = line.strip().split()

        # for loop iterates over each item in numbers_history list and assigns them to win_number
        for win_number in numbers_history:

            # try statement defines this as a block of code where exceptions can occur
            try:
                # win_number string is converted into an integer and assigned to history_integers variable
                win_num_integer = int(win_number)

                # if win_num_integer value is a key in the number_frequency dictionary, execute this code
                if win_num_integer in number_frequency:

                    # 1 is added to the value of the current key, win_num_integer, during this iteration
                    number_frequency[win_num_integer] += 1

                # if win_num_integer value is NOT a key in the number_frequency dictionary, execute this code
                else:
                    # A key is created, win_num_integer, with the value of 1
                    # The new key-value pair is added using dictionary assignment
                    number_frequency[win_num_integer] = 1

            # except statement catches the ValueError handle exception that may occur
            # ValueError is raised when an argument is received with the correct type, but invalid value
            except ValueError:

                # Prints a string informing the user that the value in win_number is not an integer
                print(f'Error: {win_number} is not an integer.')

# items method returns a key-value pair, winning number and frequency number, from the number_frequency dictionary
# key= specifies a function that determines the sorting criteria for the items of an iterable, an optional parameter
# lambda defines a small, one-line function without giving it a name, an anonymous function
# win_freq: represents each key-value pair
# win_freq[1] specifies the value to use for sorting, the second item of each pair, frequency number
# reverse= is a parameter of the sorted function. 'True' sorts the list in descending order
# sorted function returned and stored tuples into a sorted list, assigned to sorted_items variables
sorted_items = sorted(number_frequency.items(), key=lambda win_freq: win_freq[1], reverse=True)

print('lottery history'.upper())

# for loop iterates over each tuple in the sorted_items list, assigning each key and value to variables
for key_number, value_frequency in sorted_items:

    # if the value of the tuple is equal or greater than 3, execute the next code
    if value_frequency >= 3:

        # prints a literal f string of each winning number with a frequency of 3 times or more
        print(f'Winning Lottery Number:{key_number}\t Frequency: {value_frequency}')
