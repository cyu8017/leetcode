// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

public class Solution {
    public int[] OrArray(int[] nums) {
        int[] ans = new int[nums.Length - 1];
        for (int i = 1; i < nums.Length; i++) ans[i - 1] = nums[i] | nums[i - 1];
        return ans;
    }
}
