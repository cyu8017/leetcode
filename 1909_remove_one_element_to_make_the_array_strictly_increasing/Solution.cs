// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

public class Solution {
    public bool CanBeIncreasing(int[] nums) {
        bool Check(int skip) {
            int? prev = null;
            for (int i = 0; i < nums.Length; i++) {
                if (i == skip) continue;
                if (prev.HasValue && nums[i] <= prev.Value) return false;
                prev = nums[i];
            }
            return true;
        }
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] <= nums[i - 1]) return Check(i - 1) || Check(i);
        }
        return true;
    }
}