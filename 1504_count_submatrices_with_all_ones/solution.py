# LeetCode 1504

class Solution:
    def numSubmat(self, mat):
        ans = 0
        heights = [0] * len(mat[0])
        for row in mat:
            for j, x in enumerate(row):
                heights[j] = heights[j] + 1 if x else 0
            stack = []
            running = 0
            for h in heights:
                count = 1
                while stack and stack[-1][0] >= h:
                    old, width = stack.pop()
                    running -= old * width
                    count += width
                stack.append((h, count))
                running += h * count
                ans += running
        return ans
