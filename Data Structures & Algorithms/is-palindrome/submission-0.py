class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        s2=""
        for i in range(len(s)):
            if s[i]!=" " and s[i].isalnum():
                s1+="".join(s[i].lower())
                s2+="".join(s[i].lower())
        # print(s[::-1])
        if s1==s2[::-1]:
            return True
        else:
            return False