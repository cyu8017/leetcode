// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

using System;

public class Solution {
    public long MinOperations(int[] nums) {
        long ans = 0;
        for (int i = 1; i < nums.Length; i++) {
            ans += Math.Max(0L, (long)nums[i - 1] - nums[i]);
        }
        return ans;
    }
}
