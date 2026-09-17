class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChar = {}
        tChar = {}
        for i in range(len(s)):
            if s[i] in sChar:
                sChar[s[i]] += 1
            else:
                sChar[s[i]] = 1
        for i in range(len(t)):
            if t[i] in tChar:
                tChar[t[i]] += 1
            else:
                tChar[t[i]] = 1
        return sChar == tChar