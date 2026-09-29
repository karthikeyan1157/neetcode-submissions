class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=list(s)
        for i in l:
            if l.count(i)==1:
                return l.index(i)
        return -1