# LeetCode 2286 - Booking Concert Tickets in Groups
# https://leetcode.com/problems/booking-concert-tickets-in-groups/

from typing import List


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.sum = [0] * (4 * n)
        self.mx = [0] * (4 * n)
        self._build(1, 0, n - 1)

    def _pull(self, idx: int) -> None:
        self.sum[idx] = self.sum[idx * 2] + self.sum[idx * 2 + 1]
        self.mx[idx] = max(self.mx[idx * 2], self.mx[idx * 2 + 1])

    def _build(self, idx: int, l: int, r: int) -> None:
        if l == r:
            self.sum[idx] = self.mx[idx] = self.m
            return
        mid = (l + r) >> 1
        self._build(idx * 2, l, mid)
        self._build(idx * 2 + 1, mid + 1, r)
        self._pull(idx)

    def _update(self, idx: int, l: int, r: int, pos: int, val: int) -> None:
        if l == r:
            self.sum[idx] = self.mx[idx] = val
            return
        mid = (l + r) >> 1
        if pos <= mid:
            self._update(idx * 2, l, mid, pos, val)
        else:
            self._update(idx * 2 + 1, mid + 1, r, pos, val)
        self._pull(idx)

    def _querySum(self, idx: int, l: int, r: int, ql: int, qr: int) -> int:
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.sum[idx]
        mid = (l + r) >> 1
        return self._querySum(idx * 2, l, mid, ql, qr) + self._querySum(idx * 2 + 1, mid + 1, r, ql, qr)

    def _findFirst(self, idx: int, l: int, r: int, maxRow: int, k: int) -> int:
        if l > maxRow or self.mx[idx] < k:
            return -1
        if l == r:
            return l
        mid = (l + r) >> 1
        left = self._findFirst(idx * 2, l, mid, maxRow, k)
        if left != -1:
            return left
        return self._findFirst(idx * 2 + 1, mid + 1, r, maxRow, k)

    def gather(self, k: int, maxRow: int) -> List[int]:
        row = self._findFirst(1, 0, self.n - 1, maxRow, k)
        if row == -1:
            return []
        remain = self._querySum(1, 0, self.n - 1, row, row)
        seat = self.m - remain
        self._update(1, 0, self.n - 1, row, remain - k)
        return [row, seat]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self._querySum(1, 0, self.n - 1, 0, maxRow) < k:
            return False
        need = k
        row = 0
        while row <= maxRow and need > 0:
            remain = self._querySum(1, 0, self.n - 1, row, row)
            if remain != 0:
                take = min(remain, need)
                self._update(1, 0, self.n - 1, row, remain - take)
                need -= take
            row += 1
        return True
