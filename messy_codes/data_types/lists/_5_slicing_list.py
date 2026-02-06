# If we need to access a portion of a list, we can use the slicing operator, :

my_list= ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list= ", my_list)

# get list with items 2 to 4
print("my_list[2: 5]= ", my_list[2: 5])

# get list with item 2 to -3
print("my_list[2: -2]= ", my_list[2: -2])

# get list 0 to 2
print("my_list[0: 3]= ", my_list[0: 3])

# get list with 5 to last
print("my_list[5: ]= ", my_list[5: ])

# get list first to -5
print("my_list[ : -4]= ", my_list[ : -4])

# omitting both start and end index
# get list start to end index
print("my_list[:]= ", my_list[:])

