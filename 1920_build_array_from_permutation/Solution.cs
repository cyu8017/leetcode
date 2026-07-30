// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

public class Solution {
    public int[] BuildArray(int[] nums) {
        var ans = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++) ans[i] = nums[nums[i]];
        return ans;
    }
}