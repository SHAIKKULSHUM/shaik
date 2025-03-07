#creating a dictionary
student_dict = {
    "101": "Arjun",
    "102": "Bharat",
    "103": "Charmi",
    "104": "amrutha",
    "105": "anand"
}
# 1.1. Adding the values in dictionary
student_dict["106"]="babu"

# 1.2. Updating the values in dictionary
student_dict["103"] = "Charles" 

# 1.3. Accessing the value in dictionary
print(f"Student with ID 102 is: {student_dict['102']}")

# 1.4. Create a nested loop dictionary
nested_dict = {
    "ClassA": {
        "101": "Alice",
        "102": "Bob"
    },
    "ClassB": {
        "103": "Charles",
        "104": "David"
    }
}

# 1.5. Access the values of nested loop dictionary
print(f"Student with ID 103 in ClassB is: {nested_dict['ClassB']['103']}")

# 1.6. Print the keys present in a particular dictionary
print(f"Student IDs in ClassA: {list(nested_dict['ClassA'].keys())}")

# 1.7. Delete a value from a dictionary
del student_dict["101"]
print(f"Updated student dictionary: {student_dict}")
