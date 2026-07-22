// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumUniqueSubarray(int[] nums) {
        var seen = new Dictionary<int, int>();
        int left = 0, cur = 0, best = 0;
        for (int right = 0; right < nums.Length; right++) {
            int x = nums[right];
            if (seen.TryGetValue(x, out int prev) && prev >= left) {
                while (left <= prev) cur -= nums[left++];
            }
            seen[x] = right;
            cur += x;
            best = Math.Max(best, cur);
        }
        return best;
    }
}
