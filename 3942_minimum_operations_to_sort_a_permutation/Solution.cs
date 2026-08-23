// LeetCode 3942 - Minimum Operations To Sort A Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

using System;

public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        int zero = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) { zero = i; break; }
        }
        bool Check(int step) {
            for (int i = 1; i < n; i++) {
                int prev = ((zero + (i - 1) * step) % n + n) % n;
                int curr = ((zero + i * step) % n + n) % n;
                if (nums[prev] > nums[curr]) return false;
            }
            return true;
        }
        int ans = int.MaxValue;
        if (Check(1)) {
            ans = Math.Min(ans, zero);
            ans = Math.Min(ans, n - zero + 2);
        }
        if (Check(-1)) {
            ans = Math.Min(ans, zero + 2);
            ans = Math.Min(ans, n - zero);
        }
        if (ans == int.MaxValue) return -1;
        return ans;
    }
}
