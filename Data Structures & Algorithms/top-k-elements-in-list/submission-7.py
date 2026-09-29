class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
    
        for i in nums:
            d[i]=d.get(i,0)+1
        val=[[v,i] for i,v in d.items()]
        val.sort(reverse=True)
        l=[]
        while len(l)<k:
            l.append(val[len(l)][1])
        return l