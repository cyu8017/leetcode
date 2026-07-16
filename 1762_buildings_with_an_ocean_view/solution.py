class Solution:
    def findBuildings(self, heights):
        ans = []
        tallest = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > tallest:
                ans.append(i)
                tallest = heights[i]
        return ans[::-1]
