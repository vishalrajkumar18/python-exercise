letter = input("Enter a letter: ").lower()  
# gets a letter and converts it to lowercase
if letter in "aeiou" and len(letter) == 1: 
     # checks whether it is a single vowel
    print("Vowel") 
     # displays Vowel
else:
    print("Not a vowel")  
    # displays Not a vowel