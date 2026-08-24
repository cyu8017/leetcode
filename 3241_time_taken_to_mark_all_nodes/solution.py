# LeetCode 3241 - Time Taken to Mark All Nodes
# https://leetcode.com/problems/time-taken-to-mark-all-nodes/

from typing import List


class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        ans = [0] * n
        tree = [[] for _ in range(n)]
        dp = [{"top1": {"node": 0, "time": 0}, "top2": {"node": 0, "time": 0}} for _ in range(n)]
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        def getTime(u: int) -> int:
            return 2 if u % 2 == 0 else 1

        def dfs(u: int, prev: int) -> int:
            t1 = {"node": 0, "time": 0}
            t2 = {"node": 0, "time": 0}
            for v in tree[u]:
                if v == prev:
                    continue
                t = dfs(v, u) + getTime(v)
                if t >= t1["time"]:
                    t2 = t1
                    t1 = {"node": v, "time": t}
                elif t > t2["time"]:
                    t2 = {"node": v, "time": t}
            dp[u]["top1"] = t1
            dp[u]["top2"] = t2
            return t1["time"]

        def reroot(u: int, prev: int, maxTime: int) -> None:
            ans[u] = maxTime
            if dp[u]["top1"]["time"] > ans[u]:
                ans[u] = dp[u]["top1"]["time"]
            for v in tree[u]:
                if v == prev:
                    continue
                side = dp[u]["top1"]["time"]
                if dp[u]["top1"]["node"] == v:
                    side = dp[u]["top2"]["time"]
                newMax = max(maxTime, side)
                reroot(v, u, getTime(u) + newMax)

        dfs(0, -1)
        reroot(0, -1, 0)
        return ans
