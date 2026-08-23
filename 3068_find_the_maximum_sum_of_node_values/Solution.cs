// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

using System;

public class Solution {
    public long MaximumValueSum(int[] nums, int k, int[][] edges) {
        long f0 = 0, f1 = -0x3f3f3f3fL;
        foreach (int x in nums) {
            long nf0 = Math.Max(f0 + x, f1 + (x ^ k));
            long nf1 = Math.Max(f1 + x, f0 + (x ^ k));
            f0 = nf0;
            f1 = nf1;
        }
        return f0;
    }
}
