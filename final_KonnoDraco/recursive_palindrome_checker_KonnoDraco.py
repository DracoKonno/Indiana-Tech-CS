def is_palindrome_recursive(s):
    """
    Check if a string is a palindrome using recursion.
    Ignore spaces and case.
    Parameters:
    s (str): String to check
    Returns:
    bool: True if palindrome, False otherwise
    Examples:
    is_palindrome_recursive("racecar") returns True
    is_palindrome_recursive("A man a plan a canal Panama") returns True
    is_palindrome_recursive("hello") returns False
    is_palindrome_recursive("") returns True
    is_palindrome_recursive("a") returns True
    """
    # YOUR CODE HERE
    s = s.replace(" ", "").lower()

    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False

# Test your function:
print(is_palindrome_recursive("racecar")) # True
print(is_palindrome_recursive("hello")) # False
print(is_palindrome_recursive("A man a plan a canal Panama")) # True
print(is_palindrome_recursive("")) # True