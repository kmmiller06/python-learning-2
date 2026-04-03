#Beginner
import re
texts = [
"Alice is 20 years old",
"Bob is 22 years old",
"Charlie is 19 years old",
]
for text in texts:
# TODO: Use two capturing groups to extract name and age
    pattern = r"(\w+) is (\d+) years old"
match = re.search(pattern, text)
if match:
    name = match.group(1)
age = int(match.group(2))
print(f"Name: {name}, Age: {age}")
#Intermediate
import re
dates = ["03-15-2026", "12-25-2025", "01-01-2000"]
for date in dates:
# TODO 1: Write a pattern with named groups for month, day, year
# Format: MM-DD-YYYY
    pattern = r"(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})"
match = re.search(pattern, date)   
if match:
# TODO 2: Extract using named groups
    month = match.group("month")
day = match.group("day")
year = match.group("year")
info = {"month": month, "day": day, "year": year}
print(f"{info['month']}/{info['day']}/{info['year']}")
#Advanced
import re
log_entries = [
"[2026-03-10 14:30:45] Server started",
"[2026-03-10 09:15:02] User login",
"[2026-03-11 22:00:00] Backup complete",
]
for entry in log_entries:
# TODO: Write a pattern that captures date, time, and message
# The bracket section: [YYYY-MM-DD HH:MM:SS]
# Then the message after "] "
# Use named groups: date, time, message
    pattern = r"_(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})] (?P<message>.+)"
match = re.search(pattern, entry)
if match:
    d = match.groupdict()
    # The print must be indented to stay inside the if-statement
    print(f"Date: {d['date']}, Time: {d['time']}, Message: {d['message']}")
else:
    print("No match found for this entry.")
# TODO: Print formatted output  

#Unit 2 Beginner
import re
text = "The price is $49.99 today"
match = re.search(r"\$\d+\.\d{2}", text)
if match:
# TODO 1: Print the matched text
    print(f"Price: {match.group()}")
# TODO 2: Print start and end positions
# Hint: match.start(), match.end()
# TODO 3: Use span to extract everything before and after the price
start, end = match.span()
before = text[:start]
after = text[end:]
print(f"Before: '{before}'")
print(f"After: '{after}'")

#Intermediate
import re
sentences = [
"This is is a problem",
"The the cat sat down",
"No duplicates here",
"I really really like Python",
]
for sentence in sentences:
# TODO: Use a backreference to find repeated words
# Pattern: word boundary, capture a word, whitespace, same word, word boundary
    match = re.search(r"\b(\w+)\s+\1\b", sentence)
if match:
    print(f"Duplicate '{match.group(1)}' in: {sentence}")
else:
    print(f"No duplicates in: {sentence}")

#Advanced
import re
records = [
"Name: Alice Smith | ID: EMP-001 | Dept: Engineering",
"Name: Bob Jones | ID: EMP-042 | Dept: Marketing",
"Name: Carol White | ID: EMP-108 | Dept: Sales",
]
pattern = r"Name: (?P<name>.+) | ID: (?P<id>EMP-\d+) | Dept: (?P<dept>.+)"
for record in records:
    match = re.search(pattern, record)
if match:
    d = match.groupdict()
# TODO 1: Print each field using the dict
print(f"Name: {d['name']}, ID: {d['id']}, Dept: {d['dept']}")
# TODO 2: Print the position of the ID field using match.span('id')
id_span = match.span("id")
pass

#Unit 3 Beginner
import re
texts = [
"Hello there!",
"Hi everyone.",
"Hey you!",
"Goodbye now.",
"Howdy partner!"
]
for text in texts:
# TODO: Match "Hello", "Hi", or "Hey" at the start of the string
    match = re.search(r"^(Hello|Hi|Hey)", text)
if match:
    print(f"Greeting found: '{match.group(1)}' in '{text}'")
else:
    print(f"No greeting in: '{text}'")

#Intermediate
import re
files = [
"report.pdf", "photo.jpg", "data.csv",
"script.py", "style.css", "page.html",
"notes.txt", "image.png", "app.js"
]
for f in files:
    lower_f = f.lower()
# TODO 1: Match document extensions (.pdf, .doc, .txt, .csv)
is_doc = re.search(r"\.(pdf|doc|txt|csv)$", lower_f)
# TODO 2: Match image extensions (.jpg, .jpeg, .png, .gif)
is_img = re.search(r"\.(jpg|jpeg|png|gif)$", lower_f)
# TODO 3: Match code extensions (.py, .js, .html, .css)
is_code = re.search(r"\.(py|js|html|css)$", lower_f)
if is_doc:
    category = f"Document ({is_doc.group(1)})"
elif is_img:
    category = f"Image ({is_img.group(1)})"
elif is_code:
    category = f"Code ({is_code.group(1)})"
else:
    category = "Other"
print(f"{f:<15} → {category}")

#Advanced
import re
dates = [
"2026-03-15", # ISO: YYYY-MM-DD
"03/15/2026", # US: MM/DD/YYYY
"15 Mar 2026", # Text: DD Mon YYYY
"March 15, 2026", # Long: Month DD, YYYY
"not a date",
]
for date in dates:
# TODO 1: Try ISO format with named groups
    iso = re.search(r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$", date)
# TODO 2: Try US format
us = re.search(r"^(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})$", date)
# TODO 3: Try text format (3-letter month abbreviation)
text_fmt = re.search(
r"^(?P<day>\d{2}) (?P<month>[A-Za-z]{3}) (?P<year>\d{4})$",
date
)
# TODO 4: Try long format — write the pattern yourself
long_fmt = re.search(r"^(?P<month>[A-Za-z]+) (?P<day>\d{2}), (?P<year>\d{4})$", date)
matched = iso or us or text_fmt or long_fmt
if matched:
    d = matched.groupdict()
    print(f"'{date}' → month={d['month']}, day={d['day']}, year={d['year']}")
else:
    print(f"'{date}' → no match")

#Week 12 U1 Beginner
def practice_1_beginner():
    """
Beginner: Convert text to CSV
"""
print("\n" + "=" * 50)
print("EXERCISE 1.1: Text to CSV Converter")
print("=" * 50)
# Create a text file with data
with open("employees.txt", "w") as employees:
    employees.write("John Smith 35 Engineer\n")
    employees.write("Jane Doe 28 Designer\n")
    employees.write("Bob Johnson 42 Manager\n")
# TODO 1: Read text file and convert to CSV
with open("employees.txt", "r") as employees:
    with open("employees.csv", "w") as employees_csv:
# Write CSV header
        employees_csv.write("First,Last,Age,Job\n")
# TODO 1: Read text file and convert to CSV
with open("employees.txt", "r") as employees:
    with open("employees.csv", "w") as employees_csv:
        employees_csv.write("First,Last,Age,Job\n")
        
        for line in employees:
            parts = line.strip().split()
            if len(parts) >= 4:
                csv_line = f"{parts[0]},{parts[1]},{parts[2]},{parts[3]}"
                employees_csv.write(csv_line + "\n")
# Format: John,Smith,35,Engineer
# employees_csv.write(csv_line + "\n")
# TODO 2: Read and verify CSV
print("\nCSV Contents:")
with open("employees.csv", "r") as employees_csv:
# TODO: Read and display
    for line in employees_csv:
        print(line.strip())
# Run the exercise
practice_1_beginner()

#Intermediate
def practice_1_intermediate():
    """
Intermediate: Process CSV data
"""
print("\n" + "=" * 50)
print("EXERCISE 1.2: Grade Calculator")
print("=" * 50)
# Create grades CSV
with open("grades.csv", "w") as grades:
    grades.write("Student,Math,Science,English\n")
    grades.write("Alice,95,87,92\n")
    grades.write("Bob,78,85,88\n")
    grades.write("Charlie,92,94,85\n")
    grades.write("Diana,88,91,95\n")
# TODO 1: Read CSV and calculate averages
with open("grades.csv", "r") as grades:
    header = grades.readline().strip().split(",")
    print(f"Subjects: {header[1:]}")
    
    student_averages = []
    
    # This loop MUST be indented inside the 'with' block
    for line in grades:
        parts = line.strip().split(",")
        name = parts[0]
        
        # TODO: Convert parts[1:] to integers
        # We use a list comprehension to turn ['95', '87', '92'] into [95, 87, 92]
        scores = [int(s) for s in parts[1:]]
        
        # TODO: Calculate average
        # sum() adds them up, len() counts how many there are
        average = sum(scores) / len(scores)
        
        student_averages.append((name, average))
        print(f"{name}: {average:.1f}")
# TODO 2: Save results to new CSV
with open("averages.csv", "w") as averages:
    averages.write("Student,Average\n")
# TODO: Write each student's average
    for name, avg in student_averages:
        averages.write(f"{name},{avg:.1f}\n")
# Run the exercise
practice_1_intermediate()

#Advanced
def practice_1_advanced():
    """
Advanced: JSON database system
"""
print("\n" + "=" * 50)
print("EXERCISE 1.3: JSON Database")
print("=" * 50)
import json
# TODO 1: Create a product database in JSON
products = {
"inventory": [
{"id": 1, "name": "Laptop", "price": 999.99, "stock": 5},
{"id": 2, "name": "Mouse", "price": 29.99, "stock": 15},
{"id": 3, "name": "Keyboard", "price": 79.99, "stock": 8}
],
"last_updated": "2024-01-15",
"store": "Tech Store"
}
# TODO: Save to JSON file
print("Product database created")
# TODO 2: Load and modify JSON — add a new product
new_product = {
"id": 4,
"name": "Monitor",
"price": 299.99,
"stock": 3
}
# TODO: Add to inventory
products["inventory"].append(new_product)
print("Added new product: Monitor")
# TODO 3: Update stock levels
for product in products["inventory"]:
    if product["name"] == "Laptop":
        product["stock"] -= 1  # Sold one laptop
        print("Updated stock for Laptop")
# TODO 4: Save updated data
with open("products.json", "w") as f:
# TODO: Save the modified data
    json.dump(products, f)
print("Product database updated")
# TODO 5: Generate report from JSON
with open("products.json", "r") as f:
    data = json.load(f) 
# Run the exercise
practice_1_advanced()

#U2 Beginner
def practice_2_beginner():
    """
Beginner: Basic JSON operations
"""
print("\n" + "=" * 50)
print("EXERCISE 2.1: JSON Contact Card")
print("=" * 50)
import json
# TODO 1: Create a contact dictionary
contact = {
"name": "John Doe",
"email": "john@example.com",
"phone": "555-1234",
"age": 25
}
# TODO 2: Convert to JSON string
json_str = None # Replace with json.dumps(contact)
print(f"JSON String: {json_str}")
# TODO 3: Save to file
with open("contact.json", "w") as f:
# TODO: Use json.dump to save contact
    json.dump(contact, f)
print("Contact saved to file")
# TODO 4: Load from file
with open("contact.json", "r") as f:
    loaded_contact = None # Replace with json.load(f)
# TODO 5: Access data
print(f"\nLoaded contact:")
# print(f"Name: {loaded_contact['name']}")
# print(f"Email: {loaded_contact['email']}")
# Run the exercise
practice_2_beginner()

#Intermediate
def practice_2_intermediate():
    """
Intermediate: Application settings in JSON
"""
print("\n" + "=" * 50)
print("EXERCISE 2.2: Settings Manager")
print("=" * 50)
import json
# Default settings
default_settings = {
"app_name": "My App",
"version": "1.0.0",
"user_preferences": {
"theme": "dark",
"font_size": 12,
"auto_save": True
},
"recent_files": [],
"window_size": [800, 600]
}
import json

# TODO 1: Save default settings
with open("settings.json", "w") as settings_json:
    json.dump(default_settings, settings_json, indent=2)
print("Default settings created")

# TODO 2: Load and modify settings
with open("settings.json", "r") as settings_json:
    # Load the current data into a variable called 'data'
    data = json.load(settings_json)

# Now modify the dictionary (as requested in the exercise)
data["user_preferences"]["theme"] = "light"
data["recent_files"].append("project_alpha.py")

# TODO 3: Save updated settings
with open("settings.json", "w") as settings_json:
    # Use 'data' here since it contains your changes
    json.dump(data, settings_json, indent=2)

# TODO 4: Create backup
with open("settings.json", "r") as settings_json:
    backup_data = json.load(settings_json)
with open("settings_backup.json", "w") as settings_backup:
    json.dump(backup_data, settings_backup, indent=2)
print("Settings backed up")

#Advanced
def practice_2_advanced():
    """
Advanced: Mini database with JSON
"""
print("\n" + "=" * 50)
print("EXERCISE 2.3: Student Database")
print("=" * 50)
import json
# TODO 1: Create database structure
database = {"students": []}
# TODO 2: Add students function
def add_student(db, student_id, name, grades):
    """Add a student to the database"""
    student = {
        "id": student_id,
        "name": name,
        "grades": grades
    }
    db["students"].append(student)
    
# Add sample students
# add_student(database, 1001, "Alice", [95, 87, 92, 88])
# add_student(database, 1002, "Bob", [78, 85, 80, 82])
# add_student(database, 1003, "Charlie", [92, 94, 96, 91])
# TODO 3: Save database to student_db.json
with open("student_db.json", "w") as f:
    # indent=2 makes it human-readable as requested in the notes
    json.dump(database, f, indent=2)
print("Database created")

# TODO 4: Query function
def find_student(db_file, student_id):
    try:
        with open(db_file, "r") as f:
            db = json.load(f)
        for student in db["students"]:
            if student["id"] == student_id:
                return student
    except FileNotFoundError:
        print("Error: Database file not found.")
    return None

# Test query
result = find_student("student_db.json", 1001)
if result:
    print(f"\nFound: {result['name']}")
# TODO 5: Generate report
# Read database, categorize students as "high_achievers" or "needs_support"
# Save report to report.json
# Run the exercise
practice_2_advanced()
#U3 Beginner
def practice_3_beginner():
    """
Beginner: Basic pickle operations and directory creation
"""
print("\n" + "=" * 50)
print("EXERCISE 3.1: Pickle & Project Setup")
print("=" * 50)
import pickle
import os
import pickle
import os

def practice_3_beginner():
    # --- Part A: Pickle ---
    # TODO 1: Create a list to pickle 
    shopping_list = ["Apples", "Bananas", "Milk", "Bread"]

    # TODO 2: Save with pickle
    with open("shopping.pkl", "wb") as f:
        # TODO: Use pickle.dump
        pickle.dump(shopping_list, f)
    print("Shopping list pickled!")

    # TODO 3: Load with pickle
    with open("shopping.pkl", "rb") as f:
        loaded_list = pickle.load(f) # Replace with pickle.load(f)
    print(f"Loaded list: {loaded_list}")

    # TODO 4: Add items and re-save
    loaded_list.append("Eggs")
    loaded_list.append("Cheese")

    with open("shopping.pkl", "wb") as f:
        # Use pickle.dump to save the updated list
        pickle.dump(loaded_list, f)
    print("Updated list saved")

    # --- Part B: Directory Structure ---
    # TODO 5: Create project directory
    project_name = "my_project"
    if not os.path.exists(project_name):
        # TODO: Create the directory
        os.mkdir(project_name)
    print(f"Project directory '{project_name}' created")

    # TODO 6: Create subdirectories
    subdirs = ["src", "docs", "tests", "data"]
    for subdir in subdirs:
        path = os.path.join(project_name, subdir)
        # TODO: Create each subdirectory
        if not os.path.exists(path):
            os.mkdir(path)

    # TODO 7: Create initial files (README.md, main.py in src)
    with open(os.path.join(project_name, "README.md"), "w") as f:
        f.write("# My Project\nInitial documentation.")
    
    with open(os.path.join(project_name, "src", "main.py"), "w") as f:
        f.write("# Main entry point\nprint('Hello World')")

    # TODO 8: List project structure
    print("\nProject structure:")
    for root, dirs, files in os.walk(project_name):
        level = root.replace(project_name, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

# Run the exercise
practice_3_beginner()
#Intermediate
import os
import shutil
def practice_3_intermediate():
    """ Intermediate: Organize files by type """
    print("\n" + "=" * 50)
    print("EXERCISE 3.2: File Organizer")
    print("=" * 50)
    
    messy_folder = "messy_files"
    
    # --- SETUP: Create messy folder and test files ---
    # Create the main directory if it doesn't exist
    if not os.path.exists(messy_folder):
        os.mkdir(messy_folder)
        
    test_files = [
        "document.txt", "image.jpg", "photo.png",
        "report.pdf", "script.py", "data.csv",
        "music.mp3", "video.mp4", "archive.zip"
    ]
    
    # TODO: Create each file in messy_folder
    for filename in test_files:
        filepath = os.path.join(messy_folder, filename)
        with open(filepath, "w") as f:
            f.write(f"Test file: {filename}")
    print(f"Created {len(test_files)} test files in '{messy_folder}'")

    # Category mapping
    organized = {
        "documents": [".txt", ".pdf", ".doc"],
        "images": [".jpg", ".png", ".gif"],
        "code": [".py", ".js", ".html"],
        "data": [".csv", ".json", ".xml"],
        "media": [".mp3", ".mp4", ".avi"],
        "archives": [".zip", ".tar", ".rar"]
    }

    # TODO: Create organized folders for each category
    for category in organized:
        cat_path = os.path.join(messy_folder, category)
        if not os.path.exists(cat_path):
            os.mkdir(cat_path)

    # TODO: Organize files
    for filename in os.listdir(messy_folder):
        file_path = os.path.join(messy_folder, filename)
        
        # Only process files, skip the category folders themselves
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in organized.items():
                if ext in extensions:
                    # Target destination folder
                    dest_dir = os.path.join(messy_folder, category)
                    shutil.move(file_path, os.path.join(dest_dir, filename))
                    print(f"Moved '{filename}' to '{category}'")
                    moved = True
                    break
            
            if not moved:
                print(f"No category for '{filename}', leaving it in place")         

    # TODO: Show organized structure
    print("\nOrganized folder structure:")
    for root, dirs, files in os.walk(messy_folder):
        # Calculate indentation level for a clean tree view
        level = root.replace(messy_folder, "").count(os.sep)
        indent = " " * 4 * level
        folder_name = os.path.basename(root) if os.path.basename(root) else messy_folder
        print(f"{indent}{folder_name}/")
        for f in files:
            print(f"{indent}    {f}")

# Run the exercise
practice_3_intermediate()
#Advanced
def practice_3_advanced():
    """
Advanced: Complex object serialization and backup system
"""
print("\n" + "=" * 50)
print("EXERCISE 3.3: Game Save System")
print("=" * 50)
import pickle
import os
import shutil
from datetime import datetime
from pathlib import Path
# TODO 1: Create game state class
class GameState:
    def __init__(self):
        self.player_name = ""
        self.level = 1
        self.score = 0
        self.inventory = []
        self.position = (0, 0)

    def __str__(self):
        return f"{self.player_name} - Level {self.level}, Score: {self.score}"
# TODO 2: Create and populate a game state
game = GameState()
game.player_name = "Hero"
game.level = 5
game.score = 1250
game.inventory = ["Sword", "Shield", "Potion"]
game.position = (10, 25)
# TODO 3: Create saves directory and save game with pickle
saves_dir = "saves"
if not os.path.exists(saves_dir):
    os.mkdir(saves_dir)
# TODO 4: Load and verify saved game
save_path = os.path.join(saves_dir, "save1.pkl")
with open(save_path, "wb") as f:
    pickle.dump(game, f)
# Print player name, level, score, inventory, position
print(f"Player: {game.player_name}")
print(f"Level: {game.level}")
print(f"Score: {game.score}")
print(f"Inventory: {game.inventory}")
print(f"Position: {game.position}")
# TODO 5: Implement multiple save slots
def save_game(game_state, slot_number):
    """Save game to a specific slot"""
pass
# TODO 6: List all save files
def list_saves():
    """List all save files in the saves directory"""
    for filename in os.listdir(saves_dir):
        if filename.endswith(".pkl"):
            print(filename)
# TODO 7: Create backup function
def create_backup(source_dir, backup_dir="backups"):
    """Create timestamped backup of source directory"""
# Create backup directory
# Create timestamp-based folder name
# Copy entire directory
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = os.path.join(backup_data, f"backup_{timestamp}")
# TODO 8: Verify backup
def verify_backup(source, backup):
    """Check all files in source are also in backup"""
    pass
# TODO 9: Cleanup old backups (keep only most recent N)
def cleanup_old_backups(backup_dir, keep_count=3):
# Get all backups sorted by modification time
# Keep only the most recent ones
    backups = sorted(
    [f for f in os.listdir(backup_dir) if f.startswith("backup_")],
    key=lambda x: os.path.getmtime(os.path.join(backup_dir, x)),
    reverse=True
)
# Run the exercise
practice_3_advanced()