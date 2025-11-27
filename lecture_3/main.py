# Global list to store all students

students = []


def main():

    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit")
        
        choice_input = input("Enter your choice: ").strip()
        
        # Empty input protection
        if not choice_input:
            print("Please enter a valid choice.\n")
            continue
        
        # Convert to integer with error handling
        try:
            choice = int(choice_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.\n")
            continue
        
        # Exit option
        if choice == 5:
            print("Exiting program.")
            break
        # Dispatch to the correct function
        elif choice == 1:
            add_student()
        elif choice == 2:
            add_grades()
        elif choice == 3:
            generate_report()
        elif choice == 4:
            find_top_student()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


def add_student():

    name = input("Enter student name: ").strip()
    
    if not name:
        print("Student name cannot be empty.\n")
        return
    
    # Check if student already exists (case-insensitive)
    if any(s["name"].lower() == name.lower() for s in students):
        print("This student already exists.\n")
        return
    
    # Create new student record
    students.append({"name": name, "grades": []})
    print()  # Empty line for cleaner output


def add_grades():

    name = input("Enter student name: ").strip()
    
    if not name:
        print("Student name cannot be empty.\n")
        return
    
    # Find student (case-insensitive)
    student = next((s for s in students if s["name"].lower() == name.lower()), None)
    
    if not student:
        print("Student not found.\n")
        return
    
    print()  # Visual separation before grade entry
    
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()
        
        # Finish entering grades (case-insensitive)
        if grade_input.lower() == "done":
            print()  # Empty line after completion
            break
        
        # Empty input handling
        if not grade_input:
            print("Empty input. Please enter a grade or 'done'.")
            continue
        
        # Convert to float and validate range
        try:
            grade = float(grade_input)
            if not 0 <= grade <= 100:
                print("Grade must be between 0 and 100 inclusive.")
                continue
            student["grades"].append(grade)
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_report():

    print("--- Student Report ---")
    
    if not students:
        print("No students have been added yet.\n")
        return
    
    averages = []  # Collect valid averages for class statistics
    
    for student in students:
        if not student["grades"]:
            print(f"{student['name']}'s average grade is N/A.")
        else:
            avg = sum(student["grades"]) / len(student["grades"])
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)
    
    # Print class summary only if at least one student has grades
    if averages:
        print(f"Max Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {sum(averages) / len(averages):.1f}")
    
    print()  # Final empty line


def find_top_student():

    # Filter students who actually have grades
    valid_students = [s for s in students if s["grades"]]
    
    if not valid_students:
        print("There is no top student (no students added or no grades added).\n")
        return
    
    # Find student with highest average using lambda (requirement)
    top = max(valid_students, key=lambda s: sum(s["grades"]) / len(s["grades"]))
    top_avg = sum(top["grades"]) / len(top["grades"])
    
    print(f"The student with the highest average is {top['name']} with a grade of {top_avg:.1f}.\n")


# Entry point of the program
if __name__ == "__main__":
    main()