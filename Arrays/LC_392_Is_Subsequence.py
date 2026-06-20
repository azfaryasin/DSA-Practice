class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

#Second Approach
class Solution(object):
    def isSubsequence(self, s, t):
        a = 0
        n = len(s)
        b=0
        if len(s) == 0:
            return True

        for i in range(0,len(t)):
            if a < n and s[a] == t[i]:
                a +=1 
            if a == n:
                return True
        else:
            return False