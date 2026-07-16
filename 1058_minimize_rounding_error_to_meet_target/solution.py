# LeetCode 1058 - Minimize Rounding Error to Meet Target
# https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

class Solution:
    def minimizeError(self, prices: list[str], target: int) -> str:
        floors = 0
        fracs: list[float] = []
        for p in prices:
            value = float(p)
            floor = int(value)
            floors += floor
            frac = value - floor
            if frac > 1e-9:
                fracs.append(frac)
        ceil_count = target - floors
        if ceil_count < 0 or ceil_count > len(fracs):
            return "-1"
        fracs.sort(reverse=True)
        error = sum(1 - f for f in fracs[:ceil_count]) + sum(fracs[ceil_count:])
        return f"{error:.3f}"
