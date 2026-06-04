class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = ""
        for i in range(len(strs)):
            encoded += strs[i]
            if i < len(strs) - 1:
                encoded += "637@"
        return encoded
            
    def decode(self, s: str) -> List[str]:
        result = s.split("637@")
        return result

