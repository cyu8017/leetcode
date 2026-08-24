# LeetCode 3921 - Score Validator
# https://leetcode.com/problems/score-validator/

from typing import List


class Solution:
    def scoreValidator(self, events: List[str]) -> List[int]:
        score = 0
        counter = 0
        for event_str in events:
            is_num = len(event_str) > 0
            num = 0
            start = 0
            if is_num and event_str[0] == "-":
                start = 1
            for i in range(start, len(event_str)):
                if event_str[i] < "0" or event_str[i] > "9":
                    is_num = False
                    break
                num = num * 10 + (ord(event_str[i]) - 48)
            if is_num and not (start == 1 and len(event_str) == 1):
                if start == 1:
                    num = -num
                score += num
            elif event_str == "W":
                counter += 1
                if counter == 10:
                    break
            else:
                score += 1
        return [score, counter]
