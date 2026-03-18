print("Problem 1:Inventory Tracker")
class Inventory:
 def __init__(self):
    self.products = {}
 def add_product(self, name, price, quantity):
    self.products[name] = {'price': price, 'quantity': quantity}
 def sell(self, name, amount):
    if name not in self.products:
        raise ValueError(f"Product {name} not found")
    if self.products[name]['quantity'] < amount:
        raise ValueError(f"Not enough stock for {name}")
    self.products[name]['quantity'] -= amount
 def restock_report(self):
    return [name for name, info in self.products.items() if info['quantity'] < 5]
 def total_value(self):
    return sum(info['price'] * info['quantity'] for info in self.products.values())
 def most_valuable(self):
    return max(self.products.items(), key=lambda item: item[1]['price'] * item[1]['quantity'])[0]
# Test cases
inv = Inventory()
inv.add_product("Widget", 9.99, 50)
inv.add_product("Gadget", 24.99, 3)
inv.add_product("Doohickey", 4.50, 100)
inv.add_product("Thingamajig", 15.00, 2)
# Sell some items
inv.sell("Widget", 10)
print(f"Widgets after sale: {inv.products['Widget']['quantity']}")
# 40
# Restock report
print(f"Need restock: {inv.restock_report()}")
# ['Gadget', 'Thingamajig']
# Total value
print(f"Total value: ${inv.total_value():.2f}")
# $(9.99*40 + 24.99*3 + 4.50*100 + 15.00*2) = $954.57
# Most valuable product line
print(f"Most valuable: {inv.most_valuable()}")
# Doohickey (4.50 * 100 = 450.00)
# Add more of existing product
inv.add_product("Gadget", 24.99, 20)
print(f"Gadgets after restock: {inv.products['Gadget']['quantity']}")
# 23
# Error handling
try:
 inv.sell("Widget", 999)
except ValueError as e:
 print(f"Caught: {e}")
# Caught: Not enough stock for Widget
try:
 inv.sell("Nonexistent", 1)
except ValueError as e:
 print(f"Caught: {e}")
# Caught: Product Nonexistent not found

print("\nProblem 3: Image Processing Basics (NumPy)")

import numpy as np

def brightness(img, amount):
    return np.clip(img.astype(int) + amount, 0, 255).astype(np.uint8)

def contrast(img, factor):
    img = img.astype(float)
    mean = np.mean(img)
    return np.clip((img - mean) * factor + mean, 0, 255).astype(np.uint8)

def threshold(img, cutoff):
    return np.where(img >= cutoff, 255, 0).astype(np.uint8)

def crop(img, top, left, height, width):
    return img[top:top+height, left:left+width]

def statistics(img):
    mean = np.mean(img)
    std = np.std(img)
    min_val = np.min(img)
    max_val = np.max(img)
    bright_pct = np.sum(img > 200) / img.size * 100
    return {
        'mean': mean,
        'std': std,
        'min': min_val,
        'max': max_val,
        'bright_pct': bright_pct
    }

# Test cases
np.random.seed(42)
img = np.random.randint(0, 256, size=(6, 8)).astype(np.uint8)

# Brightness
bright = brightness(img, 50)
print(f"Original pixel [0,0]: {img[0, 0]}")
print(f"Brightened pixel [0,0]: {bright[0, 0]}")
# Should be original + 50, capped at 255

dark = brightness(img, -100)
print(f"Darkened pixel [0,0]: {dark[0, 0]}")
# Should be original - 100, floored at 0

# Threshold
binary = threshold(img, 128)
print(f"Binary unique values: {np.unique(binary)}")
# [0, 255]

# Crop
cropped = crop(img, 1, 2, 3, 4)
print(f"Cropped shape: {cropped.shape}")
# (3, 4)

# Statistics
stats = statistics(img)
print(f"Mean: {stats['mean']:.1f}")
print(f"Std: {stats['std']:.1f}")
print(f"Min: {stats['min']}, Max: {stats['max']}")
print(f"Bright pixels: {stats['bright_pct']:.1f}%")