class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=[]
        # l.sort(reverse=True)
        n=[]
        d={}
        for i in range(len(names)):
            l.append(heights[i])
            d[heights[i]]=d.get(names[i],names[i])
        
        # for i,v in d.items():
        #     print(i,v)
        l.sort(reverse=True)
        for i in l:
            n.append(d[i])
        return n