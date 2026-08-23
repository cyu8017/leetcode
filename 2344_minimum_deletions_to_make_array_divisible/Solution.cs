// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

using System;

public class Solution {
    public int MinOperations(int[] nums, int[] numsDivide) {
        int Gcd(int a, int b) {
            while (b != 0) { int t = a % b; a = b; b = t; }
            return a;
        }
        int g = numsDivide[0];
        for (int i = 1; i < numsDivide.Length; i++) g = Gcd(g, numsDivide[i]);
        Array.Sort(nums);
        for (int i = 0; i < nums.Length; i++)
            if (g % nums[i] == 0) return i;
        return -1;
    }
}
