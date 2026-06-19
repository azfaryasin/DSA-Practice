class Solution(object):
    def isPalindrome(self, x):
        if x <0:
            return False
        num =x
        res=0
        while x > 0:
            res = res*10+x%10
            x = x//10
        return res == num

# Second Approach
class Solution(object):
    def isPalindrome(self, x):
        if x <0:
            return False
        num = x
        res = int(str(x)[::-1])
        return res == num