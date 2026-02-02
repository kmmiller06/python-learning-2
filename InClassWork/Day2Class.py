inventory = {"apples": 50, "bananas": 30, "oranges": 45}
# Explore the types
print("=== Types ===")
print(f"keys type: {type(inventory.keys())}")
print(f"values type: {type(inventory.values())}")
print(f"items type: {type(inventory.items())}")
# View objects are dynamic
print("\n=== Dynamic Views ===")
keys_view = inventory.keys()
print(f"Before: {keys_view}")
inventory["grapes"] = 25
print(f"After adding grapes: {keys_view}")
# Memory comparison
print("\n=== Memory Usage ===")
import sys
big_dict = {i: i for i in range(10000)}
view = big_dict.keys()
as_list = list(big_dict.keys())
print(f"View: {sys.getsizeof(view)} bytes")
print(f"List: {sys.getsizeof(as_list)} bytes")
# Practical calculations
print("\n=== Calculations ===")
print(f"Products: {list(inventory.keys())}")
print(f"Total items: {sum(inventory.values())}")
print(f"Average stock: {sum(inventory.values()) / len(inventory):.1f}")
print(f"Max stock: {max(inventory.values())}")
print(f"Min stock: {min(inventory.values())}")
# Membership testing (O(1) for keys, O(n) for values)
print("\n=== Membership Tests ===")
print(f"'apples' in inventory: {'apples' in inventory}") # O(1)
print(f"50 in inventory.values(): {50 in inventory.values()}") # O(n)
# Useful methods
print("\n=== Other Methods ===")
copy_inv = inventory.copy()
print(f"Copy: {copy_inv}")
inventory.setdefault("mangos", 0) # Add if missing
print(f"After setdefault: {inventory}")
inventory.update({"apples": 60, "kiwis": 15}) # Bulk update
print(f"After update: {inventory}")