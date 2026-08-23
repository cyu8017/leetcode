// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private static final int MOD = 1000000007;

    public int countKSubsequencesWithMaxBeauty(String s, int k) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) freq[s.charAt(i) - 'a']++;
        List<Integer> vals = new ArrayList<>();
        for (int f : freq) if (f > 0) vals.add(f);
        if (vals.size() < k) return 0;
        vals.sort(Collections.reverseOrder());
        int threshold = vals.get(k - 1);
        int need = 0, avail = 0;
        long prod = 1;
        for (int v : vals) {
            if (v > threshold) {
                prod = prod * v % MOD;
                need++;
            } else if (v == threshold) avail++;
        }
        int remain = k - need;
        prod = prod * comb(avail, remain) % MOD;
        for (int i = 0; i < remain; i++) prod = prod * threshold % MOD;
        return (int) prod;
    }

    private long modPow(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    private long comb(int n, int r) {
        if (r < 0 || r > n) return 0;
        long num = 1, den = 1;
        for (int i = 0; i < r; i++) {
            num = num * (n - i) % MOD;
            den = den * (i + 1) % MOD;
        }
        return num * modPow(den, MOD - 2) % MOD;
    }
}
