class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "e"
        if not strs:
            return ""
        return "PI".join(strs)
    def decode(self, s: str) -> List[str]:
        if s=="":
            return [""]
        if s=="e":
            return []
        return s.split("PI")