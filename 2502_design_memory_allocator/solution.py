# LeetCode 2502 - Design Memory Allocator
# https://leetcode.com/problems/design-memory-allocator/


class Allocator:
    def __init__(self, n: int):
        self.mem = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        free_cnt = 0
        for i in range(len(self.mem)):
            if self.mem[i] == 0:
                free_cnt += 1
                if free_cnt == size:
                    start = i - size + 1
                    for j in range(start, i + 1):
                        self.mem[j] = mID
                    return start
            else:
                free_cnt = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        cnt = 0
        for i in range(len(self.mem)):
            if self.mem[i] == mID:
                self.mem[i] = 0
                cnt += 1
        return cnt
