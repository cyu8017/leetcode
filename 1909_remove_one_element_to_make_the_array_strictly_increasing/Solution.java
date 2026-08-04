// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution {
    public boolean canBeIncreasing(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                return check(nums, i - 1) || check(nums, i);
            }
        }
        return true;
    }

    private boolean check(int[] nums, int skip) {
        Integer prev = null;
        for (int i = 0; i < nums.length; i++) {
            if (i == skip) continue;
            if (prev != null && nums[i] <= prev) return false;
            prev = nums[i];
        }
        return true;
    }
}
