# LeetCode 2019 - The Score of Students Solving Math Expression
# https://leetcode.com/problems/the-score-of-students-solving-math-expression/

from typing import List, Set


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        def eval_correct(expr: str) -> int:
            nums, ops = [], []
            for c in expr:
                if "0" <= c <= "9":
                    nums.append(ord(c) - 48)
                else:
                    ops.append(c)
            new_nums = [nums[0]]
            new_ops = []
            for j, op in enumerate(ops):
                if op == "*":
                    new_nums[-1] *= nums[j + 1]
                else:
                    new_ops.append(op)
                    new_nums.append(nums[j + 1])
            res = new_nums[0]
            for j in range(len(new_ops)):
                res += new_nums[j + 1]
            return res

        n = len(s)
        correct = eval_correct(s)
        dp = [[None] * n for _ in range(n)]

        def dfs(l: int, r: int) -> Set[int]:
            if dp[l][r] is not None:
                return dp[l][r]
            res = set()
            if l == r:
                res.add(ord(s[l]) - 48)
                dp[l][r] = res
                return res
            for i in range(l + 1, r, 2):
                for a in dfs(l, i - 1):
                    for b in dfs(i + 1, r):
                        v = a + b if s[i] == "+" else a * b
                        if v <= 1000:
                            res.add(v)
            dp[l][r] = res
            return res

        possible = dfs(0, n - 1)
        ans = 0
        for a in answers:
            if a == correct:
                ans += 5
            elif a in possible:
                ans += 2
        return ans
