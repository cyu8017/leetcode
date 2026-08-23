// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private boolean canSubsetSum(List<Integer> vals, int target) {
        if (target == 0) return true;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int v : vals) {
            for (int s = target; s >= v; s--) if (dp[s - v]) dp[s] = true;
        }
        return dp[target];
    }

    public int minZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        if (ok(nums, queries, 0)) return 0;
        int lo = 1, hi = queries.length + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid <= queries.length && ok(nums, queries, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo > queries.length ? -1 : lo;
    }

    private boolean ok(int[] nums, int[][] queries, int k) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) continue;
            List<Integer> vals = new ArrayList<>();
            for (int q = 0; q < k; q++) {
                int l = queries[q][0], r = queries[q][1], v = queries[q][2];
                if (l <= i && i <= r) vals.add(v);
            }
            if (!canSubsetSum(vals, nums[i])) return false;
        }
        return true;
    }
}
