// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

using System;
using System.Collections.Generic;

public class Solution {
    public bool IsConsecutive(int[] nums) {
        int mn = nums[0], mx = nums[0];
        var seen = new HashSet<int>();
        foreach (int x in nums) {
            if (!seen.Add(x)) return false;
            mn = Math.Min(mn, x);
            mx = Math.Max(mx, x);
        }
        return mx - mn + 1 == nums.Length;
    }
}
