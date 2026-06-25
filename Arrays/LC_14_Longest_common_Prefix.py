class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        i=0
        s=""
        length = len(strs)
        while i < len(strs[0]):
            if strs[0][i] == strs[length-1][i]:
                s +=strs[0][i]
            else:
                break
            i+=1
        return s

# Second Approach
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
        