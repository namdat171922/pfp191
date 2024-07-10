def is_palindrome(s):
    normalized_str = s.replace(" ","").lower()
    return normalized_str == normalized_str[::-1]

print(is_palindrome("hello"))
print(is_palindrome("radar"))
print(is_palindrome("A man a plan a canal Panama"))
    