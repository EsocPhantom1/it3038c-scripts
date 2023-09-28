from datetime import datetime

def calculate_age_in_seconds(birthday):
    # Calculate the current date and time
    currentDate = datetime.now()
    # Calculate the difference between the current date and the birthday
    age = currentDate - birthday
    # Convert the age to seconds
    ageInSeconds = age.total_seconds()
    
    return ageInSeconds

# Ask the user to enter their birthday in yyyy-mm-dd format
birthdayStr = input("Enter your birthday (mm-dd-yyyy): ")

try:
    # Parse user input into datetime object
    birthday = datetime.strptime(birthdayStr, '%m-%d-%Y')
    # Calculate age in seconds
    seconds = calculate_age_in_seconds(birthday)
    # Display results
    print(f"You are approximately {seconds:.0f} seconds old.")
except ValueError:
    print("Invalid date format. Please use mm-dd-yyyy format.")
