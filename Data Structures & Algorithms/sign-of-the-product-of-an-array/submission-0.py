class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n=1
        for i in nums:
            if i>0:n*=1
            elif i<0:n*=(-1)
            else:n*=0
        return n
        