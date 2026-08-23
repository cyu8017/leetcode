// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution {
    public int maxAbsoluteSum(int[] nums) {
        int prefix = 0;
        int low = 0;
        int high = 0;
        for (int value : nums) {
            prefix += value;
            low = Math.min(low, prefix);
            high = Math.max(high, prefix);
        }
        return high - low;
    }
}
