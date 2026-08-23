// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

public class Solution {
    const int MOD = 1000000007;

    long ModPow(long a, long e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }

    public int CountGoodSubsequences(string s) {
        int[] cnt = new int[26];
        int maxf = 0;
        foreach (char c in s) {
            cnt[c - 'a']++;
            if (cnt[c - 'a'] > maxf) maxf = cnt[c - 'a'];
        }
        long[] fact = new long[maxf + 1];
        long[] invFact = new long[maxf + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxf; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxf] = ModPow(fact[maxf], MOD - 2);
        for (int i = maxf; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        long Comb(int n, int k) {
            if (k < 0 || k > n) return 0;
            return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
        }
        long ans = 0;
        for (int k = 1; k <= maxf; k++) {
            long ways = 1;
            for (int i = 0; i < 26; i++) {
                if (cnt[i] >= k) ways = ways * (1 + Comb(cnt[i], k)) % MOD;
            }
            ans = (ans + ways - 1 + MOD) % MOD;
        }
        return (int)ans;
    }
}
