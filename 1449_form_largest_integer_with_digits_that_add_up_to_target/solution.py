class Solution:
    def largestNumber(self, cost, target):
        impossible = None
        dp = [impossible] * (target + 1)
        dp[0] = ""
        for total in range(1, target + 1):
            best = impossible
            for digit in range(1, 10):
                price = cost[digit - 1]
                if total >= price and dp[total - price] is not impossible:
                    candidate = str(digit) + dp[total - price]
                    if best is impossible or (len(candidate), candidate) > (len(best), best):
                        best = candidate
            dp[total] = best
        return dp[target] if dp[target] is not impossible else "0"
