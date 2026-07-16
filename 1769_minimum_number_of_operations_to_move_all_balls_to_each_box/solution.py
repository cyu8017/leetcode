class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        ans = [0] * n
        balls = ops = 0
        for i in range(1, n):
            balls += boxes[i - 1]
            ops += balls
            ans[i] = ops
        balls = ops = 0
        for i in range(n - 2, -1, -1):
            balls += boxes[i + 1]
            ops += balls
            ans[i] += ops
        return ans
