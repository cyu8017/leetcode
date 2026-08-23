// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

public class Solution {
    public int FirstMissingPositive(int[] nums) {
        int n = nums.Length;
        int i = 0;

        while (i < n) {
            int value = nums[i];
            int target = value - 1;
            if (value >= 1 && value <= n && nums[target] != value) {
                (nums[i], nums[target]) = (nums[target], nums[i]);
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
