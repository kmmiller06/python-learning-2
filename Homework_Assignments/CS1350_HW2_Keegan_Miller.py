print("Problem 1: Movie Ratings Analyzer")
ratings = {
"Alice": {"Inception": 5, "Titanic": 3, "Avatar": 4, "Jaws": 2},
"Bob": {"Inception": 4, "The Matrix": 5, "Avatar": 5, "Jaws": 3},
"Carol": {"Titanic": 5, "The Matrix": 4, "Avatar": 3, "Interstellar": 5},
"Dave": {"Inception": 3, "Titanic": 4, "The Matrix": 5, "Jaws": 4},
"Eve": {"Inception": 5, "Avatar": 4, "Interstellar": 4, "Jaws": 1}
}
print("=== Part A:User Statistics ===")

for user, movies in ratings.items():
    num_movies = len(movies)
    avg_rating = sum(movies.values()) / num_movies

    favorite_movie = max(movies, key=movies.get)
    favorite_score = movies[favorite_movie]

    print(
        f"{user}: {num_movies} movies, "
        f"avg rating: {avg_rating:.2f}, "
        f"favorite: {favorite_movie} ({favorite_score})"
    )
   
   #Part B: Movie statistics
print("\n=== Part B: Movie Statistics ===")
   #Build a dictionary movie_stats where each movie maps to a dict containing:"ratings": list of all ratings received"avg": average rating"cont": number of ratings then print each movie with its average rating and number of reviews, sorted by average rating (highest first).
movie_stats = {}
for user_ratings in ratings.values():
         for movie, rating in user_ratings.items():
              if movie not in movie_stats:
                movie_stats[movie] = {"ratings": [], "avg": 0, "cont": 0}
              movie_stats[movie]["ratings"].append(rating)
              movie_stats[movie]["cont"] += 1
for movie, stats in movie_stats.items():
         stats["avg"] = sum(stats["ratings"]) / stats["cont"]
sorted_movies = sorted(movie_stats.items(), key=lambda x: x[1]["avg"], reverse=True)
for movie, stats in sorted_movies:
            print(f"{movie}: Avg = {stats['avg']:.2f}, Reviews = {stats['cont']}")

print("Part C: Reccommendations")
alice_rated_movies = ratings["Alice"]
recommended_movies = []
for movie, stats in movie_stats.items():
    if stats["avg"] >= 4.0 and movie not in alice_rated_movies:
        recommended_movies.append(movie)
print(f"Recommended movies for Alice: {recommended_movies}")

print("Problem 2: Sales Data Performer")
sales_records = [
{"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 5,
"region": "North"},
{"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 50,
"region": "North"},
{"product": "Desk", "category": "Furniture", "price": 350, "quantity": 8,
"region": "South"},
{"product": "Chair", "category": "Furniture", "price": 150, "quantity": 20,
"region": "South"},
{"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 3,
"region": "South"},
{"product": "Keyboard", "category": "Electronics", "price": 75, "quantity": 30, "region": "North"},
{"product": "Desk", "category": "Furniture", "price": 350, "quantity": 5,
"region": "North"},
{"product": "Monitor", "category": "Electronics", "price": 300, "quantity":
12, "region": "South"},
]
print("Part A: Dictionary Comprehensions")
# 1. product_prices
product_prices = {item["product"]: item["price"] for item in sales_records}
print("Product prices:", product_prices)

# 2. expensive_products (price > 100)
expensive_products = {
    item["product"]: item["price"]
    for item in sales_records
    if item["price"] > 100
}
print("Expensive products (>$100):", expensive_products)

# 3. price_category
price_category = {
    item["product"]: "Premium" if item["price"] >= 300 else "Standard"
    for item in sales_records
}
print("Price categories:", price_category)

print("Part B: Aggregations")

total_by_category = {}
total_by_region = {}
quantity_by_product = {}

for item in sales_records:
    revenue = item["price"] * item["quantity"]

    # 1. Revenue by category
    category = item["category"]
    total_by_category[category] = total_by_category.get(category, 0) + revenue

    # 2. Revenue by region
    region = item["region"]
    total_by_region[region] = total_by_region.get(region, 0) + revenue

    # 3. Quantity by product
    product = item["product"]
    quantity_by_product[product] = quantity_by_product.get(product, 0) + item["quantity"]

print("Revenue by category:", total_by_category)
print("Revenue by region:", total_by_region)
print("Quantity by product:", quantity_by_product)

registrations = {
    "Alice": {"CS101", "CS201", "MATH101"},
    "Bob": {"CS101", "MATH101", "PHYS101"},
    "Carol": {"CS201", "CS301", "MATH201"},
    "Dave": {"CS101", "CS201", "MATH101", "PHYS101"},
    "Eve": {"CS301", "MATH201", "MATH301"}
}

prerequisites = {
    "CS101": set(),
    "CS201": {"CS101"},
    "CS301": {"CS201"},
    "MATH101": set(),
    "MATH201": {"MATH101"},
    "MATH301": {"MATH201"},
    "PHYS101": {"MATH101"}
}

capacity = {
    "CS101": 30, "CS201": 25, "CS301": 20,
    "MATH101": 35, "MATH201": 25, "MATH301": 20,
    "PHYS101": 30
}
print("\n=== Part A: Set Operations ===")

# 1. All courses with enrollment
all_courses = set()
for courses in registrations.values():
    all_courses = all_courses | courses
print("All courses with enrollment:", all_courses)

# 2. Courses all students share
all_students = list(registrations.values())
common_courses = all_students[0]
for courses in all_students[1:]:
    common_courses = common_courses & courses
print("Courses ALL students share:", common_courses)

# 3. Courses only Alice takes
alice_courses = registrations["Alice"]
other_courses = set()
for student, courses in registrations.items():
    if student != "Alice":
        other_courses = other_courses | courses
only_alice = alice_courses - other_courses
print("Courses ONLY Alice takes:", only_alice)

# 4. Students taking CS courses
cs_students = set()
for student, courses in registrations.items():
    for course in courses:
        if course.startswith("CS"):
            cs_students.add(student)
print("Students in CS courses:", cs_students)
print("\n=== Part B: Prerequisite Check ===")

for student, courses in registrations.items():
    missing = {}

    for course in courses:
        needed = prerequisites[course]
        not_met = needed - courses
        if not_met:
            missing[course] = not_met

    if not missing:
        print(student + ": VALID")
    else:
        print(student + ": INVALID - Missing prerequisites:")
        for course, miss in missing.items():
            print(course, "requires", prerequisites[course], "but missing:", miss)
            
print("\n=== Part C: Enrollment Analysis ===")

# 1. Overloaded students (4+ courses)
overloaded = {student for student, courses in registrations.items() if len(courses) >= 4}
print("Overloaded students (4+ courses):", overloaded)

# 2. All MATH courses
math_courses = {
    course
    for courses in registrations.values()
    for course in courses
    if course.startswith("MATH")
}
print("All MATH courses enrolled:", math_courses)

# 3. Identical schedules
found = False
students = list(registrations.keys())
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if registrations[students[i]] == registrations[students[j]]:
            print("Identical schedules:", students[i], "and", students[j])
            found = True
if not found:
    print("Students with identical schedules: None found")

# 4. Enrollment per course
enrollment = {}
for courses in registrations.values():
    for course in courses:
        enrollment[course] = enrollment.get(course, 0) + 1

print("Enrollment per course:")
for course, count in enrollment.items():
    print(course + ":", count, "students")

under_enrolled = {course for course, count in enrollment.items() if count < 3}
print("Under-enrolled courses (<3 students):", under_enrolled)