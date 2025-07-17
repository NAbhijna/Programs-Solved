class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.lower()
        b = "".join(i for i in a if i.isalnum())
        if (b==b[::-1]):
            return True
        return False