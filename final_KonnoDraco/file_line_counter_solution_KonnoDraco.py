def count_lines_with_word(filename, word):
    """
    Count how many lines in a file contain a specific word.
    The search should be case-insensitive.
    Parameters:
    filename (str): Name of the file to read
    word (str): Word to search for
    Returns:
    int: Number of lines containing the word
    Returns 0 if file doesn't exist
    Example:
    If file contains:
    "Hello world"
    "Python is fun"
    "Hello again"
    count_lines_with_word("file.txt", "hello") returns 2
    """
    count = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                if word.lower() in line.lower():
                    count += 1
    except FileNotFoundError:
        print("Error: File Not Found")
    return count
test = count_lines_with_word("file.txt", "hello")