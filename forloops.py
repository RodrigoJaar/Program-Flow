number = input("enter a series of numbers with separators: ")
num = ""

for num in number:
    if num.isnumeric():
        separators = number + num

print(num)



