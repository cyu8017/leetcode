// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

using System;

public class Solution {
    void Expand(string s, int[] g, int l, int r) {
        while (l >= 0 && r < s.Length && s[l] == s[r]) {
            g[l] = Math.Max(g[l], r - l + 1);
            l--; r++;
        }
    }
    int[] Calc(string s) {
        int n = s.Length;
        int[] g = new int[n];
        for (int i = 0; i < n; i++) {
            Expand(s, g, i, i);
            Expand(s, g, i, i + 1);
        }
        return g;
    }
    public int LongestPalindrome(string s, string t) {
        int m = s.Length, n = t.Length;
        char[] tc = t.ToCharArray();
        Array.Reverse(tc);
        t = new string(tc);
        int[] g1 = Calc(s), g2 = Calc(t);
        int ans = 0;
        foreach (int v in g1) ans = Math.Max(ans, v);
        foreach (int v in g2) ans = Math.Max(ans, v);
        int[][] f = new int[m + 1][];
        for (int i = 0; i <= m; i++) f[i] = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    f[i][j] = f[i - 1][j - 1] + 1;
                    int a = (i < m) ? g1[i] : 0;
                    int b = (j < n) ? g2[j] : 0;
                    ans = Math.Max(ans, f[i][j] * 2 + a);
                    ans = Math.Max(ans, f[i][j] * 2 + b);
                }
            }
        }
        return ans;
    }
}
