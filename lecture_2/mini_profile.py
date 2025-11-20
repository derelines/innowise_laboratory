# Greet the user and prompt for the full name
user_name = input("Hello! Enter your full name: ")

# Prompt for the birth year
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)  # Convert the string input to an integer

# Calculate the current age
current_year = 2025
current_age = current_year - birth_year

# Define a function to determine the life stage based on age
def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age:
        return "Adult"
    else: 
        return "An error occurred, please write the correct age"

# Call the function to get the life stage
life_stage = generate_profile(current_age)
# Create an empty list to store hobbies
hobbies = []

# Infinite loop to collect hobbies
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)
# Create a dictionary to store the user profile
user_profile = {
    "Name": user_name,
    "Age": current_age,
    "Life Stage": life_stage,
    "Hobbies": hobbies
}

# Output the profile summary
print("---")
print("Profile Summary:")
print(f"Name: {user_profile['Name']}")
print(f"Age: {user_profile['Age']}")
print(f"Life Stage: {user_profile['Life Stage']}")

# Handle the hobbies output
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")        
