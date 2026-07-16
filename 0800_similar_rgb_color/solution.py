# LeetCode 0800 - Similar RGB Color
# https://leetcode.com/problems/similar-rgb-color/


class Solution:
    def similarRGB(self, color: str) -> str:
        def closest(component: str) -> str:
            value = int(component, 16)
            rounded = (value + 8) // 17
            return f"{rounded:x}{rounded:x}"

        return "#" + closest(color[1:3]) + closest(color[3:5]) + closest(color[5:7])
