// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

public class Solution {
    public int MakeStringSorted(string s) {
        const int MOD = 1_000_000_007;
        int n = s.Length;
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = ModPow(fact[n], MOD - 2, MOD);
        for (int i = n - 1; i >= 0; i--) invFact[i] = invFact[i + 1] * (i + 1) % MOD;

        int[] freq = new int[26];
        foreach (char ch in s) freq[ch - 'a']++;

        long ans = 0;
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            for (int smaller = 0; smaller < c; smaller++) {
                if (freq[smaller] == 0) continue;
                freq[smaller]--;
                long ways = fact[n - i - 1];
                foreach (int count in freq) ways = ways * invFact[count] % MOD;
                ans = (ans + ways) % MOD;
                freq[smaller]++;
            }
            freq[c]--;
        }
        return (int)ans;
    }

    private long ModPow(long baseVal, long exp, int mod) {
        long result = 1;
        baseVal %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) result = result * baseVal % mod;
            baseVal = baseVal * baseVal % mod;
            exp >>= 1;
        }
        return result;
    }
}
