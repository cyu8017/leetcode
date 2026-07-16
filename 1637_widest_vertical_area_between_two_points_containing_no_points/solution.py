class Solution:
    def maxWidthOfVerticalArea(self, points):
        x=sorted(p[0] for p in points)
        return max(b-a for a,b in zip(x,x[1:]))
