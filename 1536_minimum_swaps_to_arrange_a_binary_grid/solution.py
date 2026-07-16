# LeetCode 1536

class Solution:
    def minSwaps(self, grid):
        zeros = []
        for row in grid:
            count = 0
            for value in reversed(row):
                if value:
                    break
                count += 1
            zeros.append(count)
        answer, n = 0, len(grid)
        for i in range(n):
            required = n - i - 1
            j = i
            while j < n and zeros[j] < required:
                j += 1
            if j == n:
                return -1
            answer += j - i
            zeros[i:j + 1] = [zeros[j]] + zeros[i:j]
        return answer
