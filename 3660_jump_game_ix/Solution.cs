// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

using System;

public class Solution {
    public int[] MaxValue(int[] nums) {
        int n = nums.Length;
        int[] ans = new int[n], preMax = new int[n];
        preMax[0] = nums[0];
        for (int i = 1; i < n; i++) preMax[i] = Math.Max(preMax[i - 1], nums[i]);
        int sufMin = int.MaxValue / 2;
        for (int i = n - 1; i >= 0; i--) {
            if (preMax[i] > sufMin) ans[i] = ans[i + 1];
            else ans[i] = preMax[i];
            sufMin = Math.Min(sufMin, nums[i]);
        }
        return ans;
    }
}
