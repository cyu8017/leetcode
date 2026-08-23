// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinAbsoluteDifference(IList<int> nums, int x) {
        if (x == 0) {
            int ans0 = int.MaxValue;
            for (int i = 1; i < nums.Count; i++)
                ans0 = Math.Min(ans0, Math.Abs(nums[i] - nums[i - 1]));
            return ans0;
        }
        int ans = int.MaxValue;
        var arr = new SortedSet<int>();
        for (int i = x; i < nums.Count; i++) {
            arr.Add(nums[i - x]);
            int cur = nums[i];
            var view = arr.GetViewBetween(cur, int.MaxValue);
            foreach (var v in view) { ans = Math.Min(ans, v - cur); break; }
            var lower = arr.GetViewBetween(int.MinValue, cur);
            int? prev = null;
            foreach (var v in lower) prev = v;
            if (prev.HasValue) ans = Math.Min(ans, cur - prev.Value);
        }
        return ans;
    }
}
