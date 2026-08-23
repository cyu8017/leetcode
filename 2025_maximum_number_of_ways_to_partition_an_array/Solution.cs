// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int WaysToPartition(int[] nums, int k) {
        int n = nums.Length;
        long[] pref = new long[n];
        pref[0] = nums[0];
        for (int i = 1; i < n; i++) pref[i] = pref[i - 1] + nums[i];
        long total = pref[n - 1];
        var right = new Dictionary<long, int>();
        var left = new Dictionary<long, int>();
        for (int i = 0; i < n - 1; i++) {
            if (!right.ContainsKey(pref[i])) right[pref[i]] = 0;
            right[pref[i]]++;
        }
        int ans = 0;
        if (total % 2 == 0) ans = right.TryGetValue(total / 2, out int t) ? t : 0;
        for (int i = 0; i < n; i++) {
            long diff = (long)k - nums[i];
            long newTotal = total + diff;
            int cur = 0;
            if (newTotal % 2 == 0) {
                long half = newTotal / 2;
                int l = left.TryGetValue(half, out int lv) ? lv : 0;
                int r = right.TryGetValue(half - diff, out int rv) ? rv : 0;
                cur = l + r;
            }
            ans = Math.Max(ans, cur);
            if (i < n - 1) {
                if (!left.ContainsKey(pref[i])) left[pref[i]] = 0;
                left[pref[i]]++;
                right[pref[i]]--;
            }
        }
        return ans;
    }
}
