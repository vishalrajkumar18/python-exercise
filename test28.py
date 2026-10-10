numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]
# stores the given numbers in a list
for num in numbers:
    # checks each number in the list in the same order
    if num == 237:
        # checks whether the current number is 237
        break
        # stops the loop when 237 is reached
    if num % 2 == 0:
        # checks whether the number is even
        print(num)
        # displays the even number