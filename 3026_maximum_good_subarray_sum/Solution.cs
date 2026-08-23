// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumSubarraySum(int[] nums, int k) {
        var p = new Dictionary<int, long>();
        p[nums[0]] = 0;
        long s = 0;
        int n = nums.Length;
        long ans = long.MinValue;
        for (int i = 0; i < n; i++) {
            s += nums[i];
            if (p.TryGetValue(nums[i] - k, out long v1)) ans = Math.Max(ans, s - v1);
            if (p.TryGetValue(nums[i] + k, out long v2)) ans = Math.Max(ans, s - v2);
            if (i + 1 == n) break;
            if (!p.TryGetValue(nums[i + 1], out long old) || s < old) p[nums[i + 1]] = s;
        }
        return ans == long.MinValue ? 0 : ans;
    }
}
