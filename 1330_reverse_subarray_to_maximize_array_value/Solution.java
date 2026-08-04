// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

class Solution {
    public int maxValueAfterReverse(int[] nums) {
        int base = 0;
        for (int i = 0; i + 1 < nums.length; i++) base += Math.abs(nums[i] - nums[i + 1]);
        int gain = 0, low = Integer.MAX_VALUE, high = Integer.MIN_VALUE;
        for (int i = 0; i + 1 < nums.length; i++) {
            int a = nums[i], b = nums[i + 1];
            gain = Math.max(gain, Math.abs(nums[0] - b) - Math.abs(a - b));
            gain = Math.max(gain, Math.abs(nums[nums.length - 1] - a) - Math.abs(a - b));
            low = Math.min(low, Math.max(a, b));
            high = Math.max(high, Math.min(a, b));
        }
        return base + Math.max(gain, 2 * (high - low));
    }
}
