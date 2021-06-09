
name = input("please enter your name: ")
age = int(input("how hold are you, {0}? ".format(name)))

if age > 18:
    print("you are old enough to vote")
    print("please put an X in the box")
elif age == 5:
    print("sorry you are dead")
else:
    print("please come back in {0} years".format(18-age))

