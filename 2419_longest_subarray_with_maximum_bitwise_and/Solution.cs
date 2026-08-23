// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

using System;

public class Solution {
    public int LongestSubarray(int[] nums) {
        int mx = nums[0];
        foreach (int x in nums) if (x > mx) mx = x;
        int ans = 0, cur = 0;
        foreach (int x in nums) {
            if (x == mx) {
                cur++;
                ans = Math.Max(ans, cur);
            } else {
                cur = 0;
            }
        }
        return ans;
    }
}
