# LeetCode 2402 - Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/

from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x[0])
        free = []
        busy = []

        def push_free(x: int) -> None:
            free.append(x)
            i = len(free) - 1
            while i > 0:
                p = (i - 1) >> 1
                if free[p] <= free[i]:
                    break
                free[p], free[i] = free[i], free[p]
                i = p

        def pop_free() -> int:
            top = free[0]
            last = free.pop()
            if free:
                free[0] = last
                i = 0
                while True:
                    s = i
                    l, r = i * 2 + 1, i * 2 + 2
                    if l < len(free) and free[l] < free[s]:
                        s = l
                    if r < len(free) and free[r] < free[s]:
                        s = r
                    if s == i:
                        break
                    free[s], free[i] = free[i], free[s]
                    i = s
            return top

        def cmp_busy(a, b) -> int:
            if a[0] != b[0]:
                return a[0] - b[0]
            return a[1] - b[1]

        def push_busy(x) -> None:
            busy.append(x)
            i = len(busy) - 1
            while i > 0:
                p = (i - 1) >> 1
                if cmp_busy(busy[p], busy[i]) <= 0:
                    break
                busy[p], busy[i] = busy[i], busy[p]
                i = p

        def pop_busy():
            top = busy[0]
            last = busy.pop()
            if busy:
                busy[0] = last
                i = 0
                while True:
                    s = i
                    l, r = i * 2 + 1, i * 2 + 2
                    if l < len(busy) and cmp_busy(busy[l], busy[s]) < 0:
                        s = l
                    if r < len(busy) and cmp_busy(busy[r], busy[s]) < 0:
                        s = r
                    if s == i:
                        break
                    busy[s], busy[i] = busy[i], busy[s]
                    i = s
            return top

        for i in range(n):
            push_free(i)
        cnt = [0] * n
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                push_free(pop_busy()[1])
            dur = end - start
            if free:
                room = pop_free()
                begin = start
            else:
                top = pop_busy()
                begin = top[0]
                room = top[1]
            push_busy([begin + dur, room])
            cnt[room] += 1
        ans = 0
        for i in range(1, n):
            if cnt[i] > cnt[ans]:
                ans = i
        return ans
