from math import isqrt
class Solution:
    def closestDivisors(self, num):
        best=None
        for x in (num+1,num+2):
            for a in range(isqrt(x),0,-1):
                if x%a==0:
                    pair=[a,x//a]
                    if best is None or pair[1]-pair[0]<best[1]-best[0]:best=pair
                    break
        return best
