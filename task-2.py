from collections import deque


def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase
    input_string = input_string.replace(" ", "").lower()

    # Create a deque and add characters of the string
    char_deque = deque()
    for char in input_string:
        char_deque.append(char)

    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
