// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        int n = nums.length;
        long total = 0;
        for (int x : nums) {
            total += x;
        }
        int[] ans = new int[n];
        long left = 0;
        for (int i = 0; i < n; i++) {
            long x = nums[i];
            ans[i] = (int) (x * i - left + (total - left - x) - x * (n - i - 1));
            left += x;
        }
        return ans;
    }
}
