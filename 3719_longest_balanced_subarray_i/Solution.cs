// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestBalanced(int[] nums) {
        int n = nums.Length, ans = 0;
        for (int i = 0; i < n; i++) {
            var vis = new HashSet<int>();
            int[] cnt = new int[2];
            for (int j = i; j < n; j++) {
                if (!vis.Contains(nums[j])) {
                    vis.Add(nums[j]);
                    cnt[nums[j] & 1]++;
                }
                if (cnt[0] == cnt[1]) ans = Math.Max(ans, j - i + 1);
            }
        }
        return ans;
    }
}
