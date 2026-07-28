class Solution(object):
    def maxProduct(self, n):
        v=str(n)
        b=[]
        for i in range(len(v)):
            b.append(int(v[i]))
        b.sort()
        return b[-1]*b[-2]
        