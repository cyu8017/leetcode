// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

using System;
using System.Collections.Generic;

public class Solution {
    public int NumFactoredBinaryTrees(int[] arr) {
        const int MOD = 1_000_000_007;
        Array.Sort(arr);
        var dp = new Dictionary<int, long>();
        for (int i = 0; i < arr.Length; i++) {
            int x = arr[i];
            long ways = 1;
            for (int j = 0; j < i; j++) {
                int left = arr[j];
                if (x % left == 0) {
                    int right = x / left;
                    if (dp.ContainsKey(right)) ways = (ways + dp[left] * dp[right]) % MOD;
                }
            }
            dp[x] = ways;
        }
        long ans = 0;
        foreach (var v in dp.Values) ans = (ans + v) % MOD;
        return (int)ans;
    }
}
