class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=set(nums)
        for i in range(1,len(nums)+1):
            if i  in nums:
                nums.remove(i)
            else:
                nums.append(i)
        return nums