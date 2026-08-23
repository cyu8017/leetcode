// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

import java.util.Arrays;

class Solution {
    public int minOperations(int[] nums, int[] numsDivide) {
        int g = numsDivide[0];
        for (int i = 1; i < numsDivide.length; i++) g = gcd(g, numsDivide[i]);
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (g % nums[i] == 0) return i;
        }
        return -1;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
