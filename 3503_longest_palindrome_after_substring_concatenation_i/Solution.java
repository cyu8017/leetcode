// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

class Solution {
    private void expand(String s, int[] g, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            g[l] = Math.max(g[l], r - l + 1);
            l--; r++;
        }
    }

    private int[] calc(String s) {
        int n = s.length();
        int[] g = new int[n];
        for (int i = 0; i < n; i++) {
            expand(s, g, i, i);
            expand(s, g, i, i + 1);
        }
        return g;
    }

    public int longestPalindrome(String s, String t) {
        int m = s.length(), n = t.length();
        t = new StringBuilder(t).reverse().toString();
        int[] g1 = calc(s), g2 = calc(t);
        int ans = 0;
        for (int v : g1) ans = Math.max(ans, v);
        for (int v : g2) ans = Math.max(ans, v);
        int[][] f = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    f[i][j] = f[i - 1][j - 1] + 1;
                    int a = (i < m) ? g1[i] : 0;
                    int b = (j < n) ? g2[j] : 0;
                    ans = Math.max(ans, f[i][j] * 2 + a);
                    ans = Math.max(ans, f[i][j] * 2 + b);
                }
            }
        }
        return ans;
    }
}
