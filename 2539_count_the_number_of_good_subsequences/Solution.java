// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

class Solution {
    private static final int MOD = 1_000_000_007;
    private long[] fact, invFact;

    private long modPow(long a, long e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }

    private long comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
    }

    public int countGoodSubsequences(String s) {
        int[] cnt = new int[26];
        int maxf = 0;
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
            if (cnt[c - 'a'] > maxf) maxf = cnt[c - 'a'];
        }
        fact = new long[maxf + 1];
        invFact = new long[maxf + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxf; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxf] = modPow(fact[maxf], MOD - 2);
        for (int i = maxf; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        long ans = 0;
        for (int k = 1; k <= maxf; k++) {
            long ways = 1;
            for (int i = 0; i < 26; i++) {
                if (cnt[i] >= k) ways = ways * (1 + comb(cnt[i], k)) % MOD;
            }
            ans = (ans + ways - 1 + MOD) % MOD;
        }
        return (int) ans;
    }
}
