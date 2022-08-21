'''A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and 
backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char for char in s if char.isalnum())
        minu = new_string.lower()
        return minu == minu[::-1]
        

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    test = Solution()
    print(test.isPalindrome(s))
        