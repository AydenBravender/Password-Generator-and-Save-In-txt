import random

def main():
    password = []

    number_user_input = input("Do you want to include any numbers? (y/n): ")
    user_input = int(input("How many digits do you want your password to include?: "))

    if user_input < 1:
        print("Invalid input")
        return

    if number_user_input.lower() == 'y': # Adding numbers to the password
        if user_input > 1:
            user_input -= 1  # making room for the special character('#')
            password.append('#') # adds a special character
        user_input -= 1 # Decrease by 1 to make space for the random digit
        random_digit = random.randint(1, 9)
        password.append(str(random_digit))  # Convert to string before appending

    for i in range(user_input): # Generating a random letter for the specified length
        random_number = random.randint(65, 90)
        random_letter = chr(random_number)

        upper_lower_decider = random.randint(1, 2) # makes half of the letters lowercase
        if upper_lower_decider == 1:
            random_letter = random_letter.lower()

        password.append(random_letter) # Adds the letter to the password

    random.shuffle(password) # Shuffle the password for randomness
    password = ''.join(password) # removes the '' between each letter and joins them into one string

    print(password)

    save_password = input("Do you want to save the password in a txt file? (y/n): ")
    if save_password.lower() == 'y':
        filename = input("Name of file you want password saved in? add .txt at the end to save it in a txt file.: ")
        with open(filename, 'w') as file: # Open a file for writing
            file.write(password) # Write the password to the file

main()