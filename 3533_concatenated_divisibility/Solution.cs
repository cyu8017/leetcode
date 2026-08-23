// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] ConcatenatedDivisibility(int[] nums, int k) {
        Array.Sort(nums);
        int n = nums.Length;
        int[] pows = new int[n];
        for (int i = 0; i < n; i++) {
            int p = 1, num = nums[i];
            if (num == 0) p = 10 % k;
            else {
                for (int x = num; x > 0; x /= 10) p = p * 10 % k;
            }
            pows[i] = p;
        }
        var memo = new Dictionary<(int, int), bool>();
        bool Dp(int mask, int mod) {
            if (mask == (1 << n) - 1) return mod == 0;
            var kk = (mask, mod);
            if (memo.ContainsKey(kk)) return memo[kk];
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 0) {
                    int nm = (mod * pows[i] + nums[i]) % k;
                    if (Dp(mask | (1 << i), nm)) return memo[kk] = true;
                }
            }
            return memo[kk] = false;
        }
        List<int> Reconstruct(int mask, int mod) {
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 0) {
                    int nm = (mod * pows[i] + nums[i]) % k;
                    if (Dp(mask | (1 << i), nm)) {
                        var rest = Reconstruct(mask | (1 << i), nm);
                        rest.Insert(0, nums[i]);
                        return rest;
                    }
                }
            }
            return new List<int>();
        }
        if (!Dp(0, 0)) return new int[0];
        return Reconstruct(0, 0).ToArray();
    }
}
