class Solution:
    def maxDifference(self, s: str) -> int:
        a1={}
        l=[]
        for i in s:
            a1[i]=a1.get(i,0)+1
        for i in a1.values():
            l.append(i)
        l.sort(reverse=True)
        a,b=[],[]
        for i in l:
            if i%2==0:
                b.append(i)
            else:
                a.append(i)
        return (a[0]-b[-1])