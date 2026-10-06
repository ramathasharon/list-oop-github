students = ["kaisamba", "Foday", "Sharon"]
print(students)

# Accessing items in list by their index
print(f"My best friend is {students[0]} ")
print(f"My best friend is {students[1]} ")
print(f"My best friend is {students[2]} ")


# Get the index of an item in a list
print(students.index("kaisamba"))
print(students.index("Sharon"))
print(students.index("Foday"))

# know the number of items in a list
print(f"The total items in the list is: {len(students) }")

# Add items to  list
students.append("Isatu")
print(students)
students += ["Mary", "Jojo", "Marie"]

print(students)
students.insert(4, "Khart")
print(students)

# Extending a list
fruits = ["Apple","Kiwi","Mango"]
students.extend(fruits)
print(students)

# Removing an item from a list
fruits.remove("mango")


students.pop()
students.pop()
thirdItem = students.pop
print(students)
print(thirdItem)
