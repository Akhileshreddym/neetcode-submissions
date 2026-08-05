class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}
        for i in s:
            if (i in word1):
                word1[i] = word1[i] + 1
            else:
                word1[i] = 1

        for i in t:
            if (i in word2):
                word2[i] = word2[i] + 1
            else:
                word2[i] = 1
        
        return word1 == word2