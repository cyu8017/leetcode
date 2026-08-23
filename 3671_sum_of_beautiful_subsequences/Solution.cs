// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

using System;
using System.Collections.Generic;

public class Solution {
    public int TotalBeauty(int[] nums) {
        const int MOD = 1000000007;
        int mx = 0;
        foreach (int v in nums) if (v > mx) mx = v;
        var pos = new List<int>[mx + 1];
        for (int i = 0; i <= mx; i++) pos[i] = new List<int>();
        for (int i = 0; i < nums.Length; i++) pos[nums[i]].Add(i);
        int[] cnt = new int[mx + 1];
        for (int g = 1; g <= mx; g++) {
            var seq = new List<int>();
            for (int m = g; m <= mx; m += g) seq.AddRange(pos[m]);
            if (seq.Count == 0) continue;
            seq.Sort();
            int ways = 1;
            for (int i = 0; i < seq.Count; i++) ways = (int)((ways * 2L) % MOD);
            cnt[g] = (ways - 1 + MOD) % MOD;
        }
        int ans = 0;
        for (int g = mx; g >= 1; g--) {
            for (int m = 2 * g; m <= mx; m += g) {
                cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD;
            }
            ans = (int)((ans + 1L * cnt[g] * g) % MOD);
        }
        return ans;
    }
}
