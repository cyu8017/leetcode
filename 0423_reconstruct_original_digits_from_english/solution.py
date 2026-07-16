# LeetCode 0423 - Reconstruct Original Digits from English
# https://leetcode.com/problems/reconstruct-original-digits-from-english/

from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        counts = Counter(s)
        digit_counts = [0] * 10
        digit_counts[0] = counts["z"]
        digit_counts[2] = counts["w"]
        digit_counts[4] = counts["u"]
        digit_counts[6] = counts["x"]
        digit_counts[8] = counts["g"]
        digit_counts[1] = counts["o"] - digit_counts[0] - digit_counts[2] - digit_counts[4]
        digit_counts[3] = counts["h"] - digit_counts[8]
        digit_counts[5] = counts["f"] - digit_counts[4]
        digit_counts[7] = counts["s"] - digit_counts[6]
        digit_counts[9] = counts["i"] - digit_counts[5] - digit_counts[6] - digit_counts[8]
        return "".join(str(digit) * digit_counts[digit] for digit in range(10))
