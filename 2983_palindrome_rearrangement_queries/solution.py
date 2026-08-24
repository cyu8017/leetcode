# LeetCode 2983 - Palindrome Rearrangement Queries
# https://leetcode.com/problems/palindrome-rearrangement-queries/

from typing import List, Optional


def countPref(pre: List[List[int]], i: int, j: int) -> List[int]:
    cnt = [0] * 26
    for k in range(26):
        cnt[k] = pre[j + 1][k] - pre[i][k]
    return cnt


def subCnt(cnt1: List[int], cnt2: List[int]) -> Optional[List[int]]:
    cnt = [0] * 26
    for i in range(26):
        cnt[i] = cnt1[i] - cnt2[i]
        if cnt[i] < 0:
            return None
    return cnt


def eqCnt(a: List[int], b: List[int]) -> bool:
    for i in range(26):
        if a[i] != b[i]:
            return False
    return True


def check(
    pre1: List[List[int]],
    pre2: List[List[int]],
    diff: List[int],
    a: int,
    b: int,
    c: int,
    d: int,
) -> bool:
    if diff[a] > 0 or diff[len(diff) - 1] - diff[max(b, d) + 1] > 0:
        return False
    if d <= b:
        return eqCnt(countPref(pre1, a, b), countPref(pre2, a, b))
    if b < c:
        return (
            diff[c] - diff[b + 1] == 0
            and eqCnt(countPref(pre1, a, b), countPref(pre2, a, b))
            and eqCnt(countPref(pre1, c, d), countPref(pre2, c, d))
        )
    cnt1 = subCnt(countPref(pre1, a, b), countPref(pre2, a, c - 1))
    cnt2 = subCnt(countPref(pre2, c, d), countPref(pre1, b + 1, d))
    return cnt1 is not None and cnt2 is not None and eqCnt(cnt1, cnt2)


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        m = n // 2
        t = s[m:][::-1]
        s = s[:m]
        pre1 = [[0] * 26 for _ in range(m + 1)]
        pre2 = [[0] * 26 for _ in range(m + 1)]
        diff = [0] * (m + 1)
        for i in range(1, m + 1):
            for k in range(26):
                pre1[i][k] = pre1[i - 1][k]
                pre2[i][k] = pre2[i - 1][k]
            pre1[i][ord(s[i - 1]) - 97] += 1
            pre2[i][ord(t[i - 1]) - 97] += 1
            diff[i] = diff[i - 1] + (0 if s[i - 1] == t[i - 1] else 1)
        ans = []
        for i in range(len(queries)):
            q = queries[i]
            a, b = q[0], q[1]
            c, d = n - 1 - q[3], n - 1 - q[2]
            ans.append(check(pre1, pre2, diff, a, b, c, d) if a <= c else check(pre2, pre1, diff, c, d, a, b))
        return ans
