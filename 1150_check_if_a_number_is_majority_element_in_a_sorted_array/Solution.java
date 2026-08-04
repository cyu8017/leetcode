// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution {
    public boolean isMajorityElement(int[] nums, int target) {
        int left = lowerBound(nums, target);
        int right = lowerBound(nums, target + 1);
        return right - left > nums.length / 2;
    }
    private int lowerBound(int[] nums, int target) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
