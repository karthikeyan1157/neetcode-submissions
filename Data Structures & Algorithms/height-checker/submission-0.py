class Solution:
    def heightChecker(self, heights: List[int]) -> int:
            s=sorted(heights)
            c=0
            for i in range(len(s)):
                if s[i]!=heights[i]:
                    c+=1
            print(c)
            return c













