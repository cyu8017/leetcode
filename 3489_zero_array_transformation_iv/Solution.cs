// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

using System.Collections.Generic;

public class Solution {
    bool CanSubsetSum(List<int> vals, int target) {
        if (target == 0) return true;
        bool[] dp = new bool[target + 1];
        dp[0] = true;
        foreach (int v in vals) {
            for (int s = target; s >= v; s--) if (dp[s - v]) dp[s] = true;
        }
        return dp[target];
    }

    public int MinZeroArray(int[] nums, int[][] queries) {
        int n = nums.Length;
        bool Ok(int k) {
            for (int i = 0; i < n; i++) {
                if (nums[i] == 0) continue;
                var vals = new List<int>();
                for (int q = 0; q < k; q++) {
                    int l = queries[q][0], r = queries[q][1], v = queries[q][2];
                    if (l <= i && i <= r) vals.Add(v);
                }
                if (!CanSubsetSum(vals, nums[i])) return false;
            }
            return true;
        }
        if (Ok(0)) return 0;
        int lo = 1, hi = queries.Length + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid <= queries.Length && Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo > queries.Length ? -1 : lo;
    }
}
