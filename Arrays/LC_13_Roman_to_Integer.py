class Solution(object):
    def romanToInt(self, s):
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0
        n = len(s)
        a=0
        while a < n:
            if a <n-1 and d[s[a]] < d[s[a+1]]:
                res += d[s[a+1]]-d[s[a]]
                a +=2
            else:
                res += d[s[a]] 
                a+=1
        return res