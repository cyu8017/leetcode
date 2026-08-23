// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if (nums.Length <= 2) {
            return nums.Length;
        }

        int write = 2;
        for (int i = 2; i < nums.Length; i++) {
            if (nums[i] != nums[write - 2]) {
                nums[write] = nums[i];
                write++;
            }
        }

        return write;
    }
}
