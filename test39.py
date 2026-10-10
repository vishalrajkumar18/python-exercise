amt = 10000
# principal amount
interest = 3.5
# interest rate in percentage
years = 7
# number of years
future_value = amt * ((1 + (0.01 * interest)) ** years)
# computes future value using compound interest formula
print(round(future_value, 2))
# displays future value rounded to two decimal places
