// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

import java.util.Arrays;

class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int count = 0;
        for (int index = 0; index < nums.length - 2; index++) {
            int left = index + 1;
            int right = nums.length - 1;
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
