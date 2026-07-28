// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

using System.Collections.Generic;

public class Solution {
    public string LongestDupSubstring(string s) {
        int n = s.Length;
        int lo = 1, hi = n - 1, start = -1, bestLen = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int pos = Search(s, mid);
            if (pos >= 0) {
                start = pos;
                bestLen = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return start >= 0 ? s.Substring(start, bestLen) : "";
    }

    private static int Search(string s, int length) {
        const long MOD1 = 1_000_000_007L, MOD2 = 1_000_000_009L, BASE = 911382323L;
        int n = s.Length;
        long h1 = 0, h2 = 0, p1 = 1, p2 = 1;
        for (int i = 0; i < length; i++) {
            h1 = (h1 * BASE + s[i]) % MOD1;
            h2 = (h2 * BASE + s[i]) % MOD2;
            if (i > 0) { p1 = p1 * BASE % MOD1; p2 = p2 * BASE % MOD2; }
        }
        var seen = new Dictionary<(long, long), List<int>>();
        seen[(h1, h2)] = new List<int> { 0 };
        for (int i = 1; i <= n - length; i++) {
            h1 = (h1 - s[i - 1] * p1 % MOD1 + MOD1) % MOD1;
            h1 = (h1 * BASE + s[i + length - 1]) % MOD1;
            h2 = (h2 - s[i - 1] * p2 % MOD2 + MOD2) % MOD2;
            h2 = (h2 * BASE + s[i + length - 1]) % MOD2;
            var key = (h1, h2);
            if (seen.TryGetValue(key, out var list)) {
                string cur = s.Substring(i, length);
                foreach (int j in list)
                    if (s.Substring(j, length) == cur) return i;
                list.Add(i);
            } else {
                seen[key] = new List<int> { i };
            }
        }
        return -1;
    }
}
