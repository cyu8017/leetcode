// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

public class Solution {
    public void WiggleSort(int[] nums) {
        for (int index = 1; index < nums.Length; index++) {
            if (index % 2 == 1 && nums[index] < nums[index - 1]) {
                (nums[index], nums[index - 1]) = (nums[index - 1], nums[index]);
            } else if (index % 2 == 0 && nums[index] > nums[index - 1]) {
                (nums[index], nums[index - 1]) = (nums[index - 1], nums[index]);
            }
        }
    }
}
