# LeetCode 2424 - Longest Uploaded Prefix
# https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = [False] * (n + 2)
        self.prefixLen = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.uploaded[self.prefixLen + 1]:
            self.prefixLen += 1

    def longest(self) -> int:
        return self.prefixLen
