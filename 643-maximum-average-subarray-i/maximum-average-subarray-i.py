class Solution(object):
    def findMaxAverage(self, nums, k):
        a,b=0,k
        q=0
        w=[]
        for i in range(k):
            q+=nums[i]
        w.append(q)
        while b<len(nums):
            q=(q-nums[a])+nums[b]
            w.append(q)
            a+=1
            b+=1
        w=max(w)
        return (w+0.0)/k

        