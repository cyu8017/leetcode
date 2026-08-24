# LeetCode 2241 - Design an ATM Machine
# https://leetcode.com/problems/design-an-atm-machine/

from typing import List


class ATM:
    def __init__(self):
        self.cnt = [0, 0, 0, 0, 0]
        self.vals = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.cnt[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        take = [0, 0, 0, 0, 0]
        remain = amount
        tmp = self.cnt[:]
        for i in range(4, -1, -1):
            need = remain // self.vals[i]
            if need > tmp[i]:
                need = tmp[i]
            take[i] = need
            remain -= need * self.vals[i]
        if remain != 0:
            return [-1]
        for i in range(5):
            self.cnt[i] -= take[i]
        return take
