class Solution(object):
    def removeElement(self, nums, val):
        l1=nums.count(val)
        for i in range(l1):
            nums.remove(val)
        