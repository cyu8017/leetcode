from bisect import bisect_left
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        b=sorted(arr2);ans=0
        for x in arr1:
            i=bisect_left(b,x)
            ans+=not ((i<len(b) and abs(b[i]-x)<=d) or (i and abs(b[i-1]-x)<=d))
        return ans
