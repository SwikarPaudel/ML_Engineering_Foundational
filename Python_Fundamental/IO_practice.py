# Gather inputs
student_name = input("What is your name? ")
raw_classes = input("How many AI classes have you completed? ")

# Convert string input to integer for math
classes_done = int(raw_classes)
classes_left = 156 - classes_done

# Output the result cleanly using f-strings
print("\n--- Student Progress Report ---")
print(f"Student: {student_name}")
print(f"Classes Completed: {classes_done}/156")
print(f"Classes Remaining: {classes_left} more to go!")
