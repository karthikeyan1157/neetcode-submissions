class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        l = s.split()

        if len(pattern) != len(l):
            return False

        for i, j in zip(pattern, l):
            if i in d and d[i] != j:
                return False

            if i not in d:
                if j in d.values():
                    return False
                d[i] = d.get(i, j)
        print(d)
        return True
