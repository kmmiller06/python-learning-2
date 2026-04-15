#3.1 Beginner 
def practice_3_beginner():
    """
    Beginner: Basic pickle operations and directory creation
    """
print("\n" + "=" * 50)
print("EXERCISE 3.1: Pickle & Project Setup")
print("=" * 50)
import pickle
import os
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
    loaded_list = pickle.load(f)
print(f"Loaded list: {loaded_list}")
# TODO 4: Add items and re-save
loaded_list.append("Eggs")
loaded_list.append("Cheese")
with open("shopping.pkl", "wb") as f:
# TODO: Save updated list
    pickle.dump(loaded_list, f)
print("Updated list saved")
# --- Part B: Directory Structure ---
# TODO 5: Create project directory
project_name = "my_project"
if not os.path.exists(project_name):
# TODO: Create the directory
    os.makedirs(project_name)
# TODO 6: Create subdirectories
subdirs = ["src", "docs", "tests", "data"]
for subdir in subdirs:
    path = os.path.join(project_name, subdir)
    # TODO: Create each subdirectory
    os.makedirs(path, exist_ok=True)
# TODO 7: Create initial files (README.md, main.py in src)
readme_path = os.path.join(project_name, "README.md")
main_path = os.path.join(project_name, "src", "main.py")
# TODO 8: List project structure
print("\nProject structure:")
for root, dirs, files in os.walk(project_name):
    level = root.replace(project_name, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")
# Run the exercise
practice_3_beginner()

#3.2 Intermediate
def practice_3_intermediate():
    """
Intermediate: Organize files by type
"""
print("\n" + "=" * 50)
print("EXERCISE 3.2: File Organizer")
print("=" * 50)
import os
import shutil
messy_folder = "messy_files"
# TODO: Setup — Create messy folder with test files
test_files = [
"document.txt", "image.jpg", "photo.png",
"report.pdf", "script.py", "data.csv",
"music.mp3", "video.mp4", "archive.zip"
]
# TODO: Create each file in messy_folder
os.makedirs(messy_folder, exist_ok=True)
for filename in test_files:
    filepath = os.path.join(messy_folder, filename)
    with open(filepath, "w") as f:
        f.write(f"Test file: {filename}")

# Use os.path.join to create filepath
# Write "Test file: <filename>" into each file
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
    os.makedirs(os.path.join(messy_folder, category), exist_ok=True)

# TODO: Organize files
# Iterate through messy_folder
# Get file extension
# Find matching folder
# Move file to appropriate folder
for filename in os.listdir(messy_folder):
    filepath = os.path.join(messy_folder, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()
        moved = False
        for category, extensions in organized.items():
            if ext in extensions:
                dest = os.path.join(messy_folder, category, filename)
                shutil.move(filepath, dest)
                print(f"Moved {filename} to {category}/")
                moved = True
                break
        if not moved:
            print(f"No category for {filename}, leaving it in place.")
# TODO: Show organized structure
print("\nOrganized structure:")
for root, dirs, files in os.walk(messy_folder):
    level = root.replace(messy_folder, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")
# Run the exercise
practice_3_intermediate()

#3.3 Advanced
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
os.makedirs(saves_dir, exist_ok=True)
# TODO 4: Load and verify saved game
# Print player name, level, score, inventory, position
with open(os.path.join(saves_dir, "save1.pkl"), "wb") as f:
    pickle.dump(game, f)    
with open(os.path.join(saves_dir, "save1.pkl"), "rb") as f:
    loaded_game = pickle.load(f)
print("Loaded game state:")
print(f"Player: {loaded_game.player_name}")
print(f"Level: {loaded_game.level}")
print(f"Score: {loaded_game.score}")
print(f"Inventory: {loaded_game.inventory}")
print(f"Position: {loaded_game.position}")

# TODO 5: Implement multiple save slots
def save_game(game_state, slot_number):
    """Save game to a specific slot"""
    with open(os.path.join(saves_dir, f"save_{slot_number}.pkl"), "wb") as f:
        pickle.dump(game_state, f)
# TODO 6: List all save files
def list_saves():
    """List all save files in the saves directory"""
    saves = [f for f in os.listdir(saves_dir) if f.endswith(".pkl")]
    print("Available save slots:")
    for save in saves:
        print(f" - {save}")
# TODO 7: Create backup function
def create_backup(source_dir, backup_dir="backups"):
    """Create timestamped backup of source directory"""
# Create backup directory
# Create timestamp-based folder name
# Copy entire directory
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    shutil.copytree(source_dir, backup_path)
    print(f"Backup created at {backup_path}")
    return backup_path
# TODO 8: Verify backup
def verify_backup(source, backup):
    """Check all files in source are also in backup"""
    source_files = set(os.listdir(source))
    backup_files = set(os.listdir(backup))
    missing_files = source_files - backup_files
    if missing_files:
        print(f"Missing files in backup: {missing_files}")
    else:
        print("Backup verification successful! All files are present.")
# TODO 9: Cleanup old backups (keep only most recent N)
def cleanup_old_backups(backup_dir, keep_count=3):
    """Remove old backup files, keeping only the most recent N"""
    # Get all backups sorted by modification time
    backups = sorted(os.listdir(backup_dir), key=lambda x: os.path.getmtime(os.path.join(backup_dir, x)), reverse=True)
    # Keep only the most recent ones
    for backup in backups[keep_count:]:
        os.remove(os.path.join(backup_dir, backup))
# Run the exercise
practice_3_advanced()