// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int mn = nums[0], mx = nums[0];
        for (int x : nums) {
            mn = Math.min(mn, x);
            mx = Math.max(mx, x);
        }
        return Math.max(0, mx - mn - 2 * k);
    }
}
