class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += i + "637@"
        return encoded
            
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        result = s.split("637@")
        return result[:-1]

