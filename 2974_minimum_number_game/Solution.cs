// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

using System;

public class Solution {
    public int[] NumberGame(int[] nums) {
        Array.Sort(nums);
        for (int i = 0; i + 1 < nums.Length; i += 2) {
            int t = nums[i];
            nums[i] = nums[i + 1];
            nums[i + 1] = t;
        }
        return nums;
    }
}
