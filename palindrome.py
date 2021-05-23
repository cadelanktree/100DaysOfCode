def main():
    test = raw_input("Please enter a string to check for palindrome-like qualities.\n")
    print(isPalindrome(test))

def isPalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return isPalindrome(word[1:-1])


if __name__ == "__main__":
    main()
