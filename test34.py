def sum_numbers(a, b):
    # calculates the sum of two integers
    total = a + b
    # checks whether the sum is between 15 and 20 (inclusive)
    if 15 <= total <= 20:
        return 20
        # returns 20 if between 15 and 20
    else:
        return total
        # otherwise returns the original sum
print(sum_numbers(10, 6))
# displays 20 because 10 + 6 = 16 (between 15 and 20)
print(sum_numbers(10, 2))
# displays 12 because 10 + 2 = 12
print(sum_numbers(10, 12))
# displays 22 because 10 + 12 = 22
