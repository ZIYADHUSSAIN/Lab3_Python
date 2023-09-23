
numbers = []

for i in range(10):
     value = float(input(f"Enter value {i+1}: "))
     numbers.append(value)

largest = None

for number in numbers:
    if largest is None or number > largest:
        largest = number

if largest is not None:
    print("The largest number in the list is:", largest)
else:
    print("The list is empty.")
