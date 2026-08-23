// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

class Solution {
    public boolean checkPossibility(int[] nums) {
        boolean changed = false;
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] >= nums[i - 1]) {
                continue;
            }
            if (changed) {
                return false;
            }
            changed = true;
            if (i >= 2 && nums[i] < nums[i - 2]) {
                nums[i] = nums[i - 1];
            } else {
                nums[i - 1] = nums[i];
            }
        }
        return true;
    }
}
