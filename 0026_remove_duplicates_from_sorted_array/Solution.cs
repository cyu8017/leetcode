// LeetCode 0026 - Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if (nums.Length == 0) {
            return 0;
        }

        int write = 1;
        for (int read = 1; read < nums.Length; read++) {
            if (nums[read] != nums[write - 1]) {
                nums[write] = nums[read];
                write++;
            }
        }

        return write;
    }
}
