#2.1
def sum_natural(n):
    """
    Calculate sum of natural numbers from 1 to n recursively.
    Example: sum_natural(5) = 1 + 2 + 3 + 4 + 5 = 15
    """
    # TODO: Implement this
    # Hint: What's the base case? When n = 0 or n = 1?
    # Hint: How can you express sum(n) in terms of sum(n-1)?
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1)

# Test cases:
# sum_natural(5) should return 15
# sum_natural(10) should return 55
# sum_natural(1) should return 1


#2.2
def count_digits(n):
    """
    Count the number of digits in n recursively.
    Example: count_digits(1234) = 4
    Example: count_digits(7) = 1
    """
    # TODO: Implement this
    # Hint: How many digits does n // 10 have?
    # Hint: What's the base case? Single digit number?
    n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

# Test cases:
# count_digits(1234) should return 4
# count_digits(987654321) should return 9
# count_digits(5) should return 1


#2.3
def is_palindrome(s):
    """
    Check if string s is a palindrome recursively.
    Ignore case and consider only alphanumeric characters.
    Example: is_palindrome("A man a plan a canal Panama") = True
    Example: is_palindrome("race a car") = False
    """
    # TODO: Implement this
    # Hint: Compare first and last characters
    # Hint: What happens to the middle?
    # Hint: What are the base cases? (empty string, single char)
    import re
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    def helper(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(s) - 1)

# Test cases:
# is_palindrome("racecar") should return True
# is_palindrome("hello") should return False
# is_palindrome("a") should return True


#4.1
def power(x, n):
    """
    Calculate x raised to the power n recursively.
    Assume n is a non-negative integer.
    Example: power(2, 5) = 32
    Example: power(3, 0) = 1
    """
    # TODO: Implement this
    # Hint: x^n = x * x^(n-1)
    # Hint: What's x^0?
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

# Test cases:
# power(2, 5) should return 32
# power(3, 0) should return 1
# power(5, 3) should return 125


#4.2
def generate_binary_strings(n):
    """
    Generate all binary strings of length n.
    Example: generate_binary_strings(2) = ['00', '01', '10', '11']
    Example: generate_binary_strings(3) = ['000', '001', '010', '011', '100',
    '101', '110', '111']
    """
    # TODO: Implement this
    # Hint: For each position, you can place either '0' or '1'
    # Hint: Use a helper function that builds strings character by character
    result = []

    def helper(current):
        if len(current) == n:
            result.append(current)
            return
        helper(current + '0')
        helper(current + '1')

    helper('')
    return result

# Test cases:
# generate_binary_strings(2) should return ['00', '01', '10', '11']
# generate_binary_strings(1) should return ['0', '1']


def subset_sum(nums, target):
    """
    Check if any subset of nums adds up to target.
    Example: subset_sum([3, 34, 4, 12, 5, 2], 9) = True (3 + 4 + 2 = 9)
    Example: subset_sum([3, 34, 4, 12, 5, 2], 30) = False
    """
    # TODO: Implement this
    # Hint: For each number, you have two choices: include it or exclude it
    # Hint: Use index to track position in array
    def helper(i, current_sum):
        if current_sum == target:
            return True
        if i >= len(nums) or current_sum > target:
            return False
        return helper(i + 1, current_sum + nums[i]) or helper(i + 1, current_sum)

    return helper(0, 0)

# Test cases:
# subset_sum([3, 34, 4, 12, 5, 2], 9) should return True
# subset_sum([1, 2, 3, 4], 10) should return True
# subset_sum([1, 2, 3], 7) should return False


#5.1
def recursive_sum(arr, n):
    """
    Sum first n elements of array arr recursively.
    """
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Questions to answer:
# 1. Recurrence relation: T(n) = T(n-1) + O(1)
# 2. Time complexity: O(n)
# 3. Space complexity: O(n)
# 4. Recursion tree for [1,2,3,4]:
#    recursive_sum(4)
#    -> 4 + recursive_sum(3)
#    -> 4 + 3 + recursive_sum(2)
#    -> 4 + 3 + 2 + recursive_sum(1)
#    -> 4 + 3 + 2 + 1 + recursive_sum(0)


#5.2
def binary_search(arr, target, left, right):
    """
    Search for target in sorted array arr[left:right+1].
    Return index if found, -1 otherwise.
    """
    # TODO: Implement recursive binary search
    # TODO: Analyze time complexity
    # TODO: Analyze space complexity
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

# Requirements:
# 1. Implemented above
# 2. Recurrence: T(n) = T(n/2) + O(1)
# 3. Time complexity: O(log n)
# 4. Space complexity: O(log n) recursive vs O(1) iterative


#5.3
def edit_distance(s1, s2):
    """
    Find minimum edit distance between s1 and s2.
    Operations allowed: insert, delete, replace
    Example: edit_distance("cat", "cut") = 1 (replace 'a' with 'u')
    Example: edit_distance("sunday", "saturday") = 3
    """
    # TODO: Design recursive solution
    # TODO: Identify overlapping subproblems
    # TODO: Optimize with memoization
    # TODO: Analyze time complexity (both versions)

    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i

        if s1[i] == s2[j]:
            memo[(i, j)] = helper(i + 1, j + 1)
        else:
            insert = helper(i, j + 1)
            delete = helper(i + 1, j)
            replace = helper(i + 1, j + 1)
            memo[(i, j)] = 1 + min(insert, delete, replace)

        return memo[(i, j)]

    return helper(0, 0)

# Tasks:
# 1. Naive recursive: exponential time O(3^n)
# 2. Inefficient due to repeated subproblems
# 3. Memoization added above
# 4. Optimized time complexity: O(m * n), space: O(m * n)


#Merge Sort
#The complexity is that it is a divide-and-conquer algorithm that breaks down a list into smaller sublists until each sublist contains a single element. 
#It is fast because it efficiently divides the problem into smaller parts and then merges them back together in sorted order.
import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Generate 1,000,000 integers
data = [random.randint(0, 1000000) for _ in range(1000000)]

start_time = time.time()
sorted_data = merge_sort(data)
end_time = time.time()

print(f"Sorted 1,000,000 integers in {end_time - start_time:.2f} seconds")