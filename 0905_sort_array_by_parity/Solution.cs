// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

public class Solution {
    public int[] SortArrayByParity(int[] nums) {
        int i = 0;
        for (int j = 0; j < nums.Length; j++) {
            if (nums[j] % 2 == 0) {
                (nums[i], nums[j]) = (nums[j], nums[i]);
                i++;
            }
        }
        return nums;
    }
}
