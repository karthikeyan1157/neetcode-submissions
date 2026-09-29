class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(i in it for i in s)
