class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        for i in s:
            if i in s_letters:
                s_letters[i] = s_letters[i] + 1
            else:
                s_letters[i] = 1
        for i in t:
            if i in t_letters:
                t_letters[i] = t_letters[i] + 1
            else:
                t_letters[i] = 1
        return s_letters == t_letters
        