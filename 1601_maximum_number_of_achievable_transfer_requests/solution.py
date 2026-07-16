class Solution:
    def maximumRequests(self, n, requests):
        ans = 0
        for mask in range(1 << len(requests)):
            if mask.bit_count() <= ans: continue
            bal = [0] * n
            for i, (a, b) in enumerate(requests):
                if mask >> i & 1: bal[a] -= 1; bal[b] += 1
            if not any(bal): ans = mask.bit_count()
        return ans
