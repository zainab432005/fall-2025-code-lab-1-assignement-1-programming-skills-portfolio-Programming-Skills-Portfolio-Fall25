def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."
def main():
    num_input = input("Enter a number: ")
    if num_input.isdigit() or (num_input.startswith('-') and num_input[1:].isdigit()):
        num = int(num_input)
        result = check_even_odd(num)
        print(result)
    else:
        print("Invalid input! Please enter an integer.")
if __name__ == "__main__":
    main()