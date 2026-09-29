class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i]==words[j]:
                    continue
                if words[i] in words[j]:
                    if words[i] not in l:
                        l.append(words[i])
        return l