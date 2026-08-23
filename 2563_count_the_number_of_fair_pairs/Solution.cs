// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

using System;

public class Solution {
    public long CountFairPairs(int[] nums, int lower, int upper) {
        Array.Sort(nums);
        long Count(int x) {
            long ans = 0;
            int l = 0, r = nums.Length - 1;
            while (l < r) {
                if (nums[l] + nums[r] <= x) {
                    ans += r - l;
                    l++;
                } else {
                    r--;
                }
            }
            return ans;
        }
        return Count(upper) - Count(lower - 1);
    }
}
