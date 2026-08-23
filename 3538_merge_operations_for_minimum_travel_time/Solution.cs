// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinTravelTime(int l, int n, int k, int[] position, int[] time) {
        int[] prefix = new int[n];
        prefix[0] = time[0];
        for (int i = 1; i < n; i++) prefix[i] = prefix[i - 1] + time[i];
        const long Inf = (long)1e18;
        var memo = new Dictionary<(int, int, int), long>();
        long Dp(int i, int skips, int last) {
            if (i == n - 1) return skips == 0 ? 0 : Inf;
            var key = (i, skips, last);
            if (memo.ContainsKey(key)) return memo[key];
            int rate = prefix[i];
            if (last > 0) rate -= prefix[last - 1];
            long res = Inf;
            int end = n - 1;
            if (i + skips + 1 < end) end = i + skips + 1;
            for (int j = i + 1; j <= end; j++) {
                long cand = 1L * (position[j] - position[i]) * rate + Dp(j, skips - (j - i - 1), i + 1);
                if (cand < res) res = cand;
            }
            return memo[key] = res;
        }
        return (int)Dp(0, k, 0);
    }
}
