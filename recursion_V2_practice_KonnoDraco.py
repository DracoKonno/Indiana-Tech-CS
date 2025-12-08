def sum_natural(n):
    """
    Calculate sum of natural numbers from 1 to n recursively.
    Example: sum_natural(5) = 1 + 2 + 3 + 4 + 5 = 15
    """
    # TODO: Implement this
    # Hint: What's the base case? When n = 0 or n = 1?
    # Hint: How can you express sum(n) in terms of sum(n-1)?
    if n == 1:
        return 1
    else:
        return n + sum_natural(n-1)

# Test cases:
print(sum_natural(5)) #should return 15
print(sum_natural(10)) #should return 55
print(sum_natural(1)) #should return 1

def count_digits(n):
    """
    Count the number of digits in n recursively.
    Example: count_digits(1234) = 4
    Example: count_digits(7) = 1
    """
    # TODO: Implement this
    # Hint: How many digits does n // 10 have?
    # Hint: What's the base case? Single digit number?
    if 0<n<10:
        return 1
    else:
        pass
    
# Test cases:
# count_digits(1234) should return 4
# count_digits(987654321) should return 9
# count_digits(5) should return 1

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
    pass
# Test cases:
# is_palindrome("racecar") should return True
# is_palindrome("hello") should return False
# is_palindrome("a") should return True

