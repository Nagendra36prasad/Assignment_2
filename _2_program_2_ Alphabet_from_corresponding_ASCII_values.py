#Write a Python program to print a dictionary whose keys should be the alphabet from a-z
#  and the value should be corresponding ASCII values

# ASCII stands for the "American Standard Code for Information Interchange".

# we know that ASCII is a 7-bit character set containing 128 characters .
#  A-z(uppercase start with 65-90) and a-z (lowercase is start 97-122 )
# Create the dictionary
my_dict = {}
for i in range(97, 97 + 26):
  my_dict[chr(i)] = i 
print("  Ascii value of lowercase  is : ")
print(my_dict)
