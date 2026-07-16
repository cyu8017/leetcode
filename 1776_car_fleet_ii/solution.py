class Solution:
    def getCollisionTimes(self, cars):
        n = len(cars)
        ans = [-1.0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            while stack:
                j = stack[-1]
                if speed <= cars[j][1]:
                    stack.pop()
                    continue
                t = (cars[j][0] - pos) / (speed - cars[j][1])
                if ans[j] < 0 or t <= ans[j]:
                    ans[i] = t
                    break
                stack.pop()
            stack.append(i)
        return ans
