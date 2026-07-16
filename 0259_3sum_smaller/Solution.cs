// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

using System;

public class Solution {
    public int ThreeSumSmaller(int[] nums, int target) {
        Array.Sort(nums);
        int count = 0;
        for (int index = 0; index < nums.Length - 2; index++) {
            int left = index + 1;
            int right = nums.Length - 1;
            while (left < right) {
                int total = nums[index] + nums[left] + nums[right];
                if (total < target) {
                    count += right - left;
                    left++;
                } else {
                    right--;
                }
            }
        }
        return count;
    }
}
