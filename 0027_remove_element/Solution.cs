// LeetCode 0027 - Remove Element
// https://leetcode.com/problems/remove-element/

public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int write = 0;
        for (int read = 0; read < nums.Length; read++) {
            if (nums[read] != val) {
                nums[write] = nums[read];
                write++;
            }
        }
        return write;
    }
}
