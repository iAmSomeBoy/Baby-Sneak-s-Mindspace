# merging two lists

numbers= [1, 3, 5]
print('Numberrs:', numbers)

even_numbers= [2, 4, 6]
print('Even numbers:', even_numbers)

# adding elements of one list to another
numbers.extend(even_numbers)

print('Updated Numbers:', numbers)