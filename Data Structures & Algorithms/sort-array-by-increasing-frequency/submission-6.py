class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        l=[]
        for i in range(1,len(nums)):
            for j in range(len(nums)):
                if i==nums.count(nums[j]):
                    l.extend([nums[j]])
                    
        return nums if len(l)==0 else l