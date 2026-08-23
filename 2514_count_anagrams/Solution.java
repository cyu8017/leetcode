// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

class Solution {
    private static final int MOD = 1000000007;

    private long modPow(long a, long e) {
        long res = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }

    public int countAnagrams(String s) {
        String[] words = s.trim().isEmpty() ? new String[0] : s.trim().split("\\s+");
        int maxN = 0;
        for (String w : words) if (w.length() > maxN) maxN = w.length();
        long[] fact = new long[maxN + 1], invFact = new long[maxN + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxN; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxN] = modPow(fact[maxN], MOD - 2);
        for (int i = maxN; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        long ans = 1;
        for (String word : words) {
            int[] cnt = new int[26];
            for (char c : word.toCharArray()) cnt[c - 'a']++;
            long cur = fact[word.length()];
            for (int c : cnt) cur = cur * invFact[c] % MOD;
            ans = ans * cur % MOD;
        }
        return (int) ans;
    }
}
