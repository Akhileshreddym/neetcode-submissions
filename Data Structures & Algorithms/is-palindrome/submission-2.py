import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for i in s:
            if (i.isalnum()):
                stripped += i.lower()
        stripped = list(stripped)
        length = len(stripped) - 1
        for i in range(int(len(stripped))):
            if not(stripped[i] == stripped[length-i]):
                return False
        return True
        

        