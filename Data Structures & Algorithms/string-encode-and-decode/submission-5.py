class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + i
            encoded = encoded + "#&2937293^"
        return encoded
    def decode(self, s: str) -> List[str]:
        decoder = s.split("#&2937293^")
        decoded = list(decoder)
        return decoded[:-1]