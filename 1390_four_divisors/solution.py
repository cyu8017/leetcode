from math import isqrt
class Solution:
    def sumFourDivisors(self, nums):
        ans=0
        for x in nums:
            ds=set()
            for d in range(1,isqrt(x)+1):
                if x%d==0:ds|={d,x//d}
                if len(ds)>4:break
            if len(ds)==4:ans+=sum(ds)
        return ans
