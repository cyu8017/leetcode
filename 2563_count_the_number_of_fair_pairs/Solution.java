// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

import java.util.Arrays;

class Solution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        Arrays.sort(nums);
        return count(nums, upper) - count(nums, lower - 1);
    }

    private long count(int[] nums, int x) {
        long ans = 0;
        int l = 0, r = nums.length - 1;
        while (l < r) {
            if (nums[l] + nums[r] <= x) {
                ans += r - l;
                l++;
            } else r--;
        }
        return ans;
    }
}
