# LeetCode 3414 - Maximum Score of Non-overlapping Intervals
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

from typing import Dict, List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [{"l": it[0], "r": it[1], "w": it[2], "i": i} for i, it in enumerate(intervals)]
        arr.sort(key=lambda a: a["r"])

        def copyState(s: Dict) -> Dict:
            return {"score": s["score"], "idx": s["idx"][:]}

        def better(a: Dict, b: Dict) -> Dict:
            if a["score"] != b["score"]:
                return a if a["score"] > b["score"] else b
            m = min(len(a["idx"]), len(b["idx"]))
            for i in range(m):
                if a["idx"][i] != b["idx"][i]:
                    return a if a["idx"][i] < b["idx"][i] else b
            return a if len(a["idx"]) <= len(b["idx"]) else b

        dp = [[{"score": 0, "idx": []} for _ in range(5)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            cur = arr[i - 1]
            for t in range(5):
                dp[i][t] = copyState(dp[i - 1][t])
            lo, hi = 0, i - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid]["r"] < cur["l"]:
                    lo = mid + 1
                else:
                    hi = mid
            prev = lo
            for t in range(1, 5):
                prev_state = dp[prev][t - 1]
                cand = copyState(prev_state)
                cand["score"] = prev_state["score"] + cur["w"]
                cand["idx"].append(cur["i"])
                cand["idx"].sort()
                dp[i][t] = better(dp[i][t], cand)
        best = dp[n][0]
        for t in range(1, 5):
            best = better(best, dp[n][t])
        return best["idx"]
