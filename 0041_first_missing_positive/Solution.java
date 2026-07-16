// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        int i = 0;

        while (i < n) {
            int value = nums[i];
            int target = value - 1;
            if (value >= 1 && value <= n && nums[target] != value) {
                int temp = nums[i];
                nums[i] = nums[target];
                nums[target] = temp;
            } else {
                i++;
            }
        }

        for (int index = 0; index < n; index++) {
            if (nums[index] != index + 1) {
                return index + 1;
            }
        }

        return n + 1;
    }
}
