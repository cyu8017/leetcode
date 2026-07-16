# LeetCode 0359 - Logger Rate Limiter
# https://leetcode.com/problems/logger-rate-limiter/


class Logger:
    def __init__(self):
        self.last_printed: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_printed or timestamp - self.last_printed[message] >= 10:
            self.last_printed[message] = timestamp
            return True
        return False
