// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

public class Solution {
    public void MoveZeroes(int[] nums) {
        int insert = 0;
        foreach (int num in nums) {
            if (num != 0) {
                nums[insert] = num;
                insert++;
            }
        }
        for (int index = insert; index < nums.Length; index++) {
            nums[index] = 0;
        }
    }
}
