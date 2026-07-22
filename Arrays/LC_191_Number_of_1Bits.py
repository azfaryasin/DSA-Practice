class Solution(object):
    def hammingWeight(self, n):
        num = bin(n)
        res =0
        for i in num:
            if i == "1":
                res+=1
                
            else:
                continue
        return res
        










