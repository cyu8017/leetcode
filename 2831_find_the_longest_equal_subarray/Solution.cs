// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestEqualSubarray(IList<int> nums, int k) {
        var pos = new Dictionary<int, List<int>>();
        for (int i = 0; i < nums.Count; i++) {
            if (!pos.ContainsKey(nums[i])) pos[nums[i]] = new List<int>();
            pos[nums[i]].Add(i);
        }
        int ans = 0;
        foreach (var p in pos.Values) {
            int left = 0;
            for (int right = 0; right < p.Count; right++) {
                while (p[right] - p[left] - (right - left) > k) left++;
                ans = Math.Max(ans, right - left + 1);
            }
        }
        return ans;
    }
}
