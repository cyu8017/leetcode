// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

class Solution {
    public int makeStringSorted(String s) {
        int mod = 1_000_000_007;
        int n = s.length();

        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % mod;
        }

        long[] invFact = new long[n + 1];
        invFact[n] = modPow(fact[n], mod - 2, mod);
        for (int i = n - 1; i >= 0; i--) {
            invFact[i] = invFact[i + 1] * (i + 1) % mod;
        }

        int[] freq = new int[26];
        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++;
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            for (int smaller = 0; smaller < c; smaller++) {
                if (freq[smaller] == 0) {
                    continue;
                }
                freq[smaller]--;
                long ways = fact[n - i - 1];
                for (int count : freq) {
                    ways = ways * invFact[count] % mod;
                }
                ans = (ans + ways) % mod;
                freq[smaller]++;
            }
            freq[c]--;
        }

        return (int) ans;
    }

    private long modPow(long base, long exp, int mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * base % mod;
            }
            base = base * base % mod;
            exp >>= 1;
        }
        return result;
    }
}
