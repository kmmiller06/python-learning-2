#Problem 1
print("Problem 1: Word Frequency Analyzer")
def analyze_text(text):
 """
 Analyze word frequencies in text.
 Args:
 text: a string of words (may contain punctuation)
 Returns:
 dict with keys "word_counts", "most_common", "unique_count"
 """
 word_counts = {}
 for word in text.split():
     # Remove punctuation and convert to lowercase
     cleaned = ''.join(char for char in word if char.isalnum()).lower()
     if cleaned:
         word_counts[cleaned] = word_counts.get(cleaned, 0) + 1
 most_common = max(word_counts, key=word_counts.get) if word_counts else None
 return {
     "word_counts": word_counts,
     "most_common": most_common,
     "unique_count": sum(1 for count in word_counts.values() if count == 1) 
 }
# Test cases
sample = "The cat sat on the mat. The cat liked the mat!"
result = analyze_text(sample)
print(result["word_counts"])
# {'the': 4, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 2, 'liked': 1}
print(result["most_common"])
# the
print(result["unique_count"])
# 3

#Problem 3
print("\nProblem 3: Grade Statistics with NumPy")
import numpy as np
def grade_report(grades_2d):
 """
 Compute grade statistics from a 2D array (students x assignments).
 Args:
 grades_2d: numpy 2D array, shape (num_students, num_assignments)
 Returns:
 dict with keys listed above
 """
 
 student_averages = np.mean(grades_2d, axis=1)
 assignment_averages = np.mean(grades_2d, axis=0)
 highest_student = np.argmax(student_averages)
 curved_grades = grades_2d + 5  # Simple curve
 passing = curved_grades >= 60
 return {
     "student_averages": student_averages,
     "assignment_averages": assignment_averages,
     "highest_student": highest_student,
     "curved_grades": curved_grades,
     "passing": passing
 }
# Test cases
grades = np.array([
 [85, 90, 78, 92], # Student 0
 [70, 65, 80, 75], # Student 1
 [95, 88, 92, 97], # Student 2
 [60, 72, 68, 55] # Student 3
])
report = grade_report(grades)
print("Student averages:", report["student_averages"])
# [86.25 72.5 93. 63.75]
print("Assignment averages:", report["assignment_averages"])
# [77.5 78.75 79.5 79.75]
print("Highest student index:", report["highest_student"])
# 2
print("Curved grades (Student 0):", report["curved_grades"][0])
# [91.40 96.77 83.87 98.92] (approximately)
print("Passing (Student 3):", report["passing"][3])
# [ True True True False]
