// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

using System.Collections.Generic;

public class Solution {
    public int DistinctEchoSubstrings(string text) {
        int n = text.Length;
        long mod1 = 1000000007, mod2 = 1000000009, bas = 911382323;
        var h1 = new long[n + 1]; var h2 = new long[n + 1];
        var p1 = new long[n + 1]; var p2 = new long[n + 1];
        p1[0] = p2[0] = 1;
        for (int i = 0; i < n; i++) {
            int code = text[i];
            h1[i + 1] = (h1[i] * bas + code) % mod1;
            h2[i + 1] = (h2[i] * bas + code) % mod2;
            p1[i + 1] = p1[i] * bas % mod1;
            p2[i + 1] = p2[i] * bas % mod2;
        }
        (long, long) Hashed(int left, int right) {
            int length = right - left;
            long a = (h1[right] - h1[left] * p1[length] % mod1 + mod1) % mod1;
            long b = (h2[right] - h2[left] * p2[length] % mod2 + mod2) % mod2;
            return (a, b);
        }
        var echoes = new HashSet<(int, long, long)>();
        for (int half = 1; half <= n / 2; half++) {
            for (int left = 0; left <= n - 2 * half; left++) {
                if (Hashed(left, left + half).Equals(Hashed(left + half, left + 2 * half))) {
                    var h = Hashed(left, left + 2 * half);
                    echoes.Add((2 * half, h.Item1, h.Item2));
                }
            }
        }
        return echoes.Count;
    }
}
