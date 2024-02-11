# Created a list of values as strings, ending with a new line \n and assigned to the lines variable
lines = ['In the sea so blue,\n', 'with a flip and a "woo-hoo,"\n', 'dolphins play and jest,\n',
         'showing who\'s the best.\n\n']

# with statement automatically closes the file after this block of code is executed
# open function opens the file dolphin.txt in 'append and read' a+ mode as the variable, dolphin_file
# 'append and read' mode opens the file for both reading and writing. If the file does not exist, it creates a new file.
with open('dolphin.txt', 'a+') as dolphin_file:

    # .write() method writes only a single string onto dolphin.txt
    # .write() method does not include separators or formatting. So \n new lines were included in this string.
    dolphin_file.write('Dolphins have names for each other.'
                       '\n\nThey use a "signature" whistle to identify themselves '
                       'to other dolphins in their group.\n\n')

    # for loop iterates over each value/string in the list, lines variable, and assigns it to dolphin_rhyme variable
    for dolphin_rhyme in lines:

        # .writelines() method writes multiple strings from any iterable object, like the list, to a file
        # .writelines() method also does not include formatting or line separators
        # The \n in the lines list values indicates the end of a line for the .writelines() method
        dolphin_file.writelines(dolphin_rhyme)

# Created an empty list and assigned it to the dolphin_word_list variable
dolphin_word_list = []

# Created an empty list and assigned it to the dolphin_line_list variable
dolphin_line_list = []

# with statement automatically closes the file after this block of code is executed
# open() function opens the dolphin.txt file in read mode, for reading only, as the dolphin_file variable
with open('dolphin.txt', 'r') as dolphin_file:

    # the next function returns the next item in an iterable object, like iterator
    # An iterator is an object that allows sequential access to elements in a stream of data.
    # A file object returned by the open() function is an iterator
    # next() reads the next line from the file and returns it. In this case, it is the 1st line stored in a variable
    first_line = next(dolphin_file)

    # A string about the returned data type is printed, including the type of the first_line variable
    print('The returned data type from dolphin.txt is:', type(first_line), '\n')

    # .seek() method changes the current position of the file pointer within a file
    # 0 indicates the beginning of the file, bringing the file pointer to the start of the dolphin.txt file
    dolphin_file.seek(0)

    # for loop iterates over each line in dolphin.txt and stores it in the line variable
    for line in dolphin_file:

        # .strip() method removes whitespace from both ends of a string
        # if a line contains any non-white space characters to apply .strip() on, execute the next code
        # if there are ONLY white spaces on a line, do NOT execute the next code
        if line.strip():

            # strip() removes the white space from the start and end of each line
            # append() method adds a single element to the end of a list
            # append() adds the whole string line as a value in dolphin_line_list
            dolphin_line_list.append(line.strip())

            # split() method converts the line to a list, using space as the default separator for values
            # extend() method adds elements of an iterable, the new list, to the end of a list, dolphin_word_list
            dolphin_word_list.extend(line.split())

# prints the dolphin_word_list and a string about the number of values that list has
print(f'{dolphin_word_list}\n\nThis list has {len(dolphin_word_list)} values.\n\n')

# prints each line in dolphin.txt without any empty lines
# for loop iterates over each value in dolphin_line_list and stores it in line
for line in dolphin_line_list:

    # each value or line is printed
    print(line)
