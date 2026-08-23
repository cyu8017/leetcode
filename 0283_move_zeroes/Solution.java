// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

class Solution {
    public void moveZeroes(int[] nums) {
        int insert = 0;
        for (int num : nums) {
            if (num != 0) {
                nums[insert] = num;
                insert++;
            }
        }
        for (int index = insert; index < nums.length; index++) {
            nums[index] = 0;
        }
    }
}
