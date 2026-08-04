// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

import java.util.*;

class Solution {
    public int distinctEchoSubstrings(String text) {
        int n = text.length();
        long mod1 = 1_000_000_007L, mod2 = 1_000_000_009L, base = 911382323L;
        long[] h1 = new long[n + 1], h2 = new long[n + 1];
        long[] p1 = new long[n + 1], p2 = new long[n + 1];
        p1[0] = p2[0] = 1;
        for (int i = 0; i < n; i++) {
            int code = text.charAt(i);
            h1[i + 1] = (h1[i] * base + code) % mod1;
            h2[i + 1] = (h2[i] * base + code) % mod2;
            p1[i + 1] = p1[i] * base % mod1;
            p2[i + 1] = p2[i] * base % mod2;
        }
        Set<String> echoes = new HashSet<>();
        for (int half = 1; half <= n / 2; half++) {
            for (int left = 0; left <= n - 2 * half; left++) {
                long[] a = hash(h1, h2, p1, p2, mod1, mod2, left, left + half);
                long[] b = hash(h1, h2, p1, p2, mod1, mod2, left + half, left + 2 * half);
                if (a[0] == b[0] && a[1] == b[1]) {
                    long[] full = hash(h1, h2, p1, p2, mod1, mod2, left, left + 2 * half);
                    echoes.add(half * 2 + ":" + full[0] + ":" + full[1]);
                }
            }
        }
        return echoes.size();
    }

    private long[] hash(long[] h1, long[] h2, long[] p1, long[] p2, long mod1, long mod2, int left, int right) {
        int length = right - left;
        long x1 = (h1[right] - h1[left] * p1[length] % mod1 + mod1) % mod1;
        long x2 = (h2[right] - h2[left] * p2[length] % mod2 + mod2) % mod2;
        return new long[]{x1, x2};
    }
}
