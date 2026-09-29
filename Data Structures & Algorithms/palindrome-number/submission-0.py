class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        r=n[::-1]
        return (n==r)