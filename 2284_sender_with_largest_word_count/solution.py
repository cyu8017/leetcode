# LeetCode 2284 - Sender With Largest Word Count
# https://leetcode.com/problems/sender-with-largest-word-count/

from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        count = {}
        best = ""
        best_cnt = -1
        for i, msg in enumerate(messages):
            words = 1
            for c in msg:
                if c == " ":
                    words += 1
            c2 = count.get(senders[i], 0) + words
            count[senders[i]] = c2
            if c2 > best_cnt or (c2 == best_cnt and senders[i] > best):
                best_cnt = c2
                best = senders[i]
        return best
