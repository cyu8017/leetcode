# LeetCode 2129 - Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        parts = title.strip().split()
        for i in range(len(parts)):
            w = parts[i].lower()
            if len(w) > 2:
                w = w[0].upper() + w[1:]
            parts[i] = w
        return " ".join(parts)
