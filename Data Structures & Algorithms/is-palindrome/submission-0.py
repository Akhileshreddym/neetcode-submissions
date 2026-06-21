class Solution:
    def isPalindrome(self, s: str) -> bool:
        string2 = ""
        for i in s:
            if(i.isalnum()):
                string2 += i.lower()
        s = string2
        

        for i in range(int((len(s)/2))):
            if (s[i] == s[(len(s) - 1 - i)]):
                continue
            else:
                return False
        return True