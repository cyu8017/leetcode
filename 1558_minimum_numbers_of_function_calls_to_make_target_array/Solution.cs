// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

using System;

public class Solution {
    public int MinOperations(int[] nums) {
        int adds = 0, maxShift = 0;
        foreach (int x in nums) {
            adds += PopCount(x);
            if (x > 0) maxShift = Math.Max(maxShift, BitLength(x) - 1);
        }
        return adds + maxShift;
    }

    private static int PopCount(int x) {
        int c = 0;
        while (x > 0) { c += x & 1; x >>= 1; }
        return c;
    }

    private static int BitLength(int x) {
        int len = 0;
        while (x > 0) { len++; x >>= 1; }
        return len;
    }
}
