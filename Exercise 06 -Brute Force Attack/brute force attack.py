correct_password = "12345"
max_attempts = 5 
attempts = 0

while attempts < max_attempts:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password! You have {remaining} attempts left.\n")
        else:
            print("Maximum attempts reached! Authorities have been alerted.")