// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinimumIncompatibility(int[] nums, int k) {
        int n = nums.Length;
        int size = n / k;
        int full = (1 << n) - 1;
        var groups = new Dictionary<int, int>();
        for (int mask = 0; mask < (1 << n); mask++) {
            if (BitCount(mask) != size) continue;
            var vals = new List<int>();
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) vals.Add(nums[i]);
            }
            if (vals.Distinct().Count() == size)
                groups[mask] = vals.Max() - vals.Min();
        }

        var memo = new Dictionary<int, int>();
        int Dp(int mask) {
            if (mask == full) return 0;
            if (memo.TryGetValue(mask, out int cached)) return cached;
            int first = 0;
            while (((mask >> first) & 1) == 1) first++;
            int best = int.MaxValue / 2;
            foreach (var (g, c) in groups) {
                if (((g >> first) & 1) == 1 && (g & mask) == 0)
                    best = Math.Min(best, c + Dp(mask | g));
            }
            return memo[mask] = best;
        }

        int ans = Dp(0);
        return ans >= int.MaxValue / 2 ? -1 : ans;
    }

    private static int BitCount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }
}
