name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Invalid input! Please enter a number.")
print(name, hometown, age, sep="\n")