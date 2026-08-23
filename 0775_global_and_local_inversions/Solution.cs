// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

using System;

public class Solution {
    public bool IsIdealPermutation(int[] nums) {
        for (int i = 0; i < nums.Length; i++) {
            if (Math.Abs(nums[i] - i) > 1) return false;
        }
        return true;
    }
}
