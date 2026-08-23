// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

using System;

public class Solution {
    public bool IsMajorityElement(int[] nums, int target) {
        int left = LowerBound(nums, target);
        int right = LowerBound(nums, target + 1);
        return (right - left) > nums.Length / 2;
    }

    private int LowerBound(int[] nums, int target) {
        int lo = 0, hi = nums.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
