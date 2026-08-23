// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

using System;

public class Solution {
    public int MaximizeScore(int[] nums) {
        int n = nums.Length;
        int total = 0;
        foreach (int x in nums) total += x;
        if (n % 2 == 1) {
            int mn = nums[0];
            foreach (int x in nums) if (x < mn) mn = x;
            return total - mn;
        }
        int mn2 = nums[0] + nums[1];
        for (int i = 0; i + 1 < n; i++) mn2 = Math.Min(mn2, nums[i] + nums[i + 1]);
        return total - mn2;
    }
}
