class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        l=list(set(allowed))
        l.sort()
        n=[]
        c=0
        for i in words:
            m=list(set(i))
            m.sort()
            n.append(m)
        for i in range(len(n)):
            c1=1
            for j in range(len(n[i])):
                if n[i][j] not in l:
                    c1=0
            if c1==1:
                c+=1
        return c