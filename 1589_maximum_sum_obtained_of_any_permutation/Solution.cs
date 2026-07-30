// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

using System;

public class Solution {
    public int MaxSumRangeQuery(int[] nums, int[][] requests) {
        const int MOD = 1000000007;
        int[] diff = new int[nums.Length + 1];
        foreach (var r in requests) {
            diff[r[0]]++;
            diff[r[1] + 1]--;
        }
        for (int i = 1; i < nums.Length; i++) diff[i] += diff[i - 1];
        Array.Sort(nums);
        Array.Sort(diff, 0, nums.Length);
        long sum = 0;
        for (int i = 0; i < nums.Length; i++) sum += (long)nums[i] * diff[i];
        return (int)(sum % MOD);
    }
}
