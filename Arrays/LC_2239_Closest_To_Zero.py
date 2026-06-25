class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for i in nums:
            if abs(i) == abs(closest):
                closest = max(closest,i)
            elif abs(i) < abs(closest):
                closest = i
        
        return closest
#


