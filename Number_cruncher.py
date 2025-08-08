user_input = input("Enter the number separated by commas: ")
# 3, 90, 875, 59, 5, 7, 10, 45, 87
parts = user_input.split(",")

numbers = list(map(float,[p.strip() for p in parts]))

print("Input : ", numbers)

length = len(numbers)
print("Lenght of the list : ", length)

Sum = sum(numbers)
print("Sum of the numbers in the list : ", Sum)

avg = Sum // length
print("Average of the numbers :", avg)

minimum = min(numbers)
maximum = max(numbers)
print("Maximum number in the list : ", maximum)
print("Minimum number in the list : ", minimum)

absolute_values = [abs(num) for num in numbers]
print("Absolute numbers : ", absolute_values)

sort = sorted(numbers)
reverse_sort = sorted(numbers, reverse=True) 

print("Ascending order : " ,sort)
print("Desending order : " ,reverse_sort)

#a = sort[::-1]
#print(a)
indexed_list = list(enumerate(numbers, start= 1))
print("Indexed list : ", indexed_list)


for i in numbers:
    q, r = divmod(i, 10) # The number after i is our preferable number not in nuilt or must use
    print(f"The Quotient of {i} is: {q} \nThe Remainder of {i} is: {r}")
    print()

positive = all(num > 0 for num in numbers)
print("All the numbers in the list is Positive : ", positive)

negative = any(num < 0 for num in numbers)
print("All the numbers in the list is Negative : ", negative)
    
