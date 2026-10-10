def histogram(numbers):
    # defines a function to create a histogram from a list of integers
    for num in numbers:
        # takes each number from the list one by one
        print('*' * num)
        # prints the star symbol according to the value of the number
histogram([1,2,3 ,4 ])
# calls the function with a list of numbers to display the histogram