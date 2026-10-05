class Solution(object):
    def reverse(self, x):
        is_negative=x<0
        x=abs(x)
        reverse=0
        while x>0:
            reverse=reverse*10+x%10
            x//=10
        if is_negative:
            reverse=-reverse
        if reverse<-2**31 or reverse>2**31-1:
            return 0
        return reverse


        