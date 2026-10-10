color_list_1 = set(["White", "Black", "Red"])
# stores the first group of colors in a set
color_list_2 = set(["Red", "Green"])
# stores the second group of colors in a set
result = color_list_1 - color_list_2
# removes the colors in color_list_2 from color_list_1
print(result)
# displays the remaining colors