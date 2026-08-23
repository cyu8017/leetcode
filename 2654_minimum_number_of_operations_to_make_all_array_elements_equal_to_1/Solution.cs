// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

using System;

public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length, ones = 0;
        foreach (int x in nums) if (x == 1) ones++;
        if (ones > 0) return n - ones;
        int Gcd(int a, int b) { while (b != 0) { int t = a % b; a = b; b = t; } return a; }
        int best = n + 1;
        for (int i = 0; i < n; i++) {
            int g = 0;
            for (int j = i; j < n; j++) {
                g = Gcd(g, nums[j]);
                if (g == 1) { best = Math.Min(best, j - i); break; }
            }
        }
        if (best == n + 1) return -1;
        return best + n - 1;
    }
}
