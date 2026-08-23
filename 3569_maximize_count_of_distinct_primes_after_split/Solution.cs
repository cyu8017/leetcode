// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] MaximumCount(int[] nums, int[][] queries) {
        int mx = 0;
        foreach (int v in nums) mx = Math.Max(mx, v);
        foreach (var q in queries) mx = Math.Max(mx, q[1]);
        bool[] isP = new bool[mx + 1];
        for (int i = 2; i <= mx; i++) isP[i] = true;
        for (int i = 2; i * i <= mx; i++) {
            if (isP[i]) {
                for (int j = i * i; j <= mx; j += i) isP[j] = false;
            }
        }
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            nums[queries[qi][0]] = queries[qi][1];
            int best = 0;
            var left = new Dictionary<int, int>();
            var right = new Dictionary<int, int>();
            foreach (int v in nums) {
                if (v <= mx && isP[v]) {
                    if (!right.ContainsKey(v)) right[v] = 0;
                    right[v]++;
                }
            }
            for (int i = 0; i < nums.Length - 1; i++) {
                int v = nums[i];
                if (v <= mx && isP[v]) {
                    if (!left.ContainsKey(v)) left[v] = 0;
                    left[v]++;
                    if (--right[v] == 0) right.Remove(v);
                }
                best = Math.Max(best, left.Count + right.Count);
            }
            ans[qi] = best;
        }
        return ans;
    }
}
