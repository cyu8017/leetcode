// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

using System;

public class Solution {
    public long MaxScore(int[] nums, int x) {
        long NEG = -(1L << 60);
        long even = nums[0], odd = nums[0];
        if (nums[0] % 2 == 0) odd = NEG;
        else even = NEG;
        for (int i = 1; i < nums.Length; i++) {
            long v = nums[i];
            if (nums[i] % 2 == 0) even = Math.Max(even + v, odd + v - x);
            else odd = Math.Max(odd + v, even + v - x);
        }
        return Math.Max(even, odd);
    }
}
