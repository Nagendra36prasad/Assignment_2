# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Iterating through a tuple via for loop
# Nested for loops - comparing original tuple with the sorted 2nd element list.

lst1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lst2 =[]
lst3 =[]

for i in lst1:
    lst2.append(i[1],)

lst2.sort()
print(lst2)

for j in lst2:
    for k in lst1:
        if j == int(k[1],):
            lst3.append(k)
print("sorted in increasing order by the last element in each tuple given list  is : ")
print(lst3)

