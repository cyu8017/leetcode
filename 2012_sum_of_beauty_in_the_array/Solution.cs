// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

using System;

public class Solution {
    public int SumOfBeauties(int[] nums) {
        int n = nums.Length;
        int[] prefixMax = new int[n], suffixMin = new int[n];
        prefixMax[0] = nums[0];
        for (int i = 1; i < n; i++) prefixMax[i] = Math.Max(prefixMax[i - 1], nums[i]);
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) suffixMin[i] = Math.Min(suffixMin[i + 1], nums[i]);
        int ans = 0;
        for (int i = 1; i < n - 1; i++) {
            if (prefixMax[i - 1] < nums[i] && nums[i] < suffixMin[i + 1]) ans += 2;
            else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) ans++;
        }
        return ans;
    }
}
