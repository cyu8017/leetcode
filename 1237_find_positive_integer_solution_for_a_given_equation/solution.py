class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> list[list[int]]:
        answer, x, y = [], 1, 1000
        while x <= 1000 and y >= 1:
            value = customfunction.f(x, y)
            if value == z:
                answer.append([x, y])
                x += 1
                y -= 1
            elif value < z: x += 1
            else: y -= 1
        return answer
