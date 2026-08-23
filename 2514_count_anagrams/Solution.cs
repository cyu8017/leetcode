// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

using System;

public class Solution {
    private const int MOD = 1000000007;

    public int CountAnagrams(string s) {
        string[] words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int maxN = 0;
        foreach (string w in words) if (w.Length > maxN) maxN = w.Length;
        long[] fact = new long[maxN + 1], invFact = new long[maxN + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxN; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxN] = ModPow(fact[maxN], MOD - 2);
        for (int i = maxN; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        long ans = 1;
        foreach (string word in words) {
            int[] cnt = new int[26];
            foreach (char c in word) cnt[c - 'a']++;
            long cur = fact[word.Length];
            foreach (int c in cnt) cur = cur * invFact[c] % MOD;
            ans = ans * cur % MOD;
        }
        return (int)ans;
    }

    private long ModPow(long a, long e) {
        long res = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
}
