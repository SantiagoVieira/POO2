if __name__ == "__main__":
    def is_palindrome(text):
        text = text.lower()
        text = text.replace(" ", "")
        return text == text[::-1]

input_text = input("Enter a text: ")

if is_palindrome(input_text):
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")