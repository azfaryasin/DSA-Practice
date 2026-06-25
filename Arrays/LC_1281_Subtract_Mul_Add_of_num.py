class Solution(object):
    def subtractProductAndSum(self, n):
        x = n
        res = 0
        s=0
        m=1
        while x>0:
            res = x%10
            s+=res
            m*=res
            x=x//10
        return m-s


