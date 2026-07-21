class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        radius = [0] * n
        center = right = 0
        for i in range(n):
            if i < right:
                radius[i] = min(right - i, radius[2 * center - i])
            while (
                i - radius[i] - 1 >= 0
                and i + radius[i] + 1 < n
                and s[i - radius[i] - 1] == s[i + radius[i] + 1]
            ):
                radius[i] += 1
            if i + radius[i] > right:
                center, right = i, i + radius[i]

        end = [1] * n
        start = [1] * n
        for i in range(n):
            r = radius[i]
            end[i + r] = max(end[i + r], 2 * r + 1)
            start[i - r] = max(start[i - r], 2 * r + 1)
        for i in range(n - 2, -1, -1):
            end[i] = max(end[i], end[i + 1] - 2)
        for i in range(1, n):
            start[i] = max(start[i], start[i - 1] - 2)

        pre = [0] * n
        pre[0] = end[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], end[i])
        suf = [0] * n
        suf[-1] = start[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i + 1], start[i])

        return max(pre[i] * suf[i + 1] for i in range(n - 1))
