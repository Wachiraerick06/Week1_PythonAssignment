# Empty list
my_list = []

# Append elements to the list

my_list.append( 10)
my_list.append( 20)
my_list.append( 30)
my_list.append( 40)

print(my_list)
# Insert elements
my_list.insert(1, 15)

print(my_list)

      # extend the list

my_list.extend([50, 60, 70])
print(my_list)
# Remove Elements
my_list.remove(70)
print(my_list)

# sorting in ascending order
my_list.sort()
print(my_list)

# Finding an index of an element
index = my_list.index(30)
print(index)
