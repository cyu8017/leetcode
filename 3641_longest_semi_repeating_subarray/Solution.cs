// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestSubarray(int[] nums, int k) {
        var cnt = new Dictionary<int, int>();
        int ans = 0, cur = 0, l = 0;
        for (int r = 0; r < nums.Length; r++) {
            if (!cnt.ContainsKey(nums[r])) cnt[nums[r]] = 0;
            if (++cnt[nums[r]] == 2) cur++;
            while (cur > k) {
                if (--cnt[nums[l]] == 1) cur--;
                l++;
            }
            ans = Math.Max(ans, r - l + 1);
        }
        return ans;
    }
}
