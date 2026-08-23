// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

using System;

public class Solution {
    public int TwoSumLessThanK(int[] nums, int k) {
        Array.Sort(nums);
        int lo = 0, hi = nums.Length - 1, ans = -1;
        while (lo < hi) {
            int total = nums[lo] + nums[hi];
            if (total < k) {
                ans = Math.Max(ans, total);
                lo++;
            } else {
                hi--;
            }
        }
        return ans;
    }
}
