# LeetCode 2621 - Sleep
# https://leetcode.com/problems/sleep/

import time


class Solution:
    def sleep(self, millis: int):
        time.sleep(millis / 1000.0)
        return None
