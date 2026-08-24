# LeetCode 3295 - Report Spam Message
# https://leetcode.com/problems/report-spam-message/

from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        ban = set(bannedWords)
        cnt = 0
        for w in message:
            if w in ban:
                cnt += 1
                if cnt >= 2:
                    return True
        return False
