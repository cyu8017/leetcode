// LeetCode 1498 - Number Of Subsequences That Satisfy The Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

using System;
public class Solution {
    public int NumSubseq(int[] nums, int target) {
        Array.Sort(nums);
        int mod = 1000000007, left = 0, right = nums.Length - 1, ans = 0;
        var powers = new int[nums.Length + 1]; powers[0] = 1;
        for (int i = 1; i < powers.Length; i++) powers[i] = powers[i - 1] * 2 % mod;
        while (left <= right) {
            if (nums[left] + nums[right] <= target) { ans = (ans + powers[right - left]) % mod; left++; }
            else right--;
        }
        return ans;
    }
}
