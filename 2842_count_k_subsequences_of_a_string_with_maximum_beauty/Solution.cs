// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

using System;
using System.Collections.Generic;

public class Solution {
    const int MOD = 1000000007;

    long ModPow(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    long Comb(int n, int r) {
        if (r < 0 || r > n) return 0;
        long num = 1, den = 1;
        for (int i = 0; i < r; i++) {
            num = num * (n - i) % MOD;
            den = den * (i + 1) % MOD;
        }
        return num * ModPow(den, MOD - 2) % MOD;
    }

    public int CountKSubsequencesWithMaxBeauty(string s, int k) {
        int[] freq = new int[26];
        foreach (char c in s) freq[c - 'a']++;
        var vals = new List<int>();
        foreach (int f in freq) if (f > 0) vals.Add(f);
        if (vals.Count < k) return 0;
        vals.Sort((a, b) => b.CompareTo(a));
        int threshold = vals[k - 1];
        int need = 0, avail = 0;
        long prod = 1;
        foreach (int v in vals) {
            if (v > threshold) { prod = prod * v % MOD; need++; }
            else if (v == threshold) avail++;
        }
        int remain = k - need;
        prod = prod * Comb(avail, remain) % MOD;
        for (int i = 0; i < remain; i++) prod = prod * threshold % MOD;
        return (int)prod;
    }
}
