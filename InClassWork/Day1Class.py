pet = {"name": "Buddy", "type": "dog", "age": 3}
print(f"Name: {pet['name']}, Type: {pet['type']}, Age: {pet['age']}")
print(f"Color: {pet.get('color', 'Unknown')}")

grades = {"Jay": 85, "Mia": 92, "Sam": 48}
for student, grade in grades.items():
    status = "Passed" if grade >= 50 else "Failed"
    print(f"{student}: {grade} - {status}")
    
menu = {"Burger": 5.99, "Fries": 2.99, "Soda": 1.50}
expensive = [item for item, price in menu.items() if price > 15]