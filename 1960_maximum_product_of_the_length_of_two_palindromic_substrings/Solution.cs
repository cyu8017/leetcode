// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

using System;

public class Solution {
    public long MaxProduct(string s) {
        int n = s.Length;
        var radius = new int[n];
        int center = 0, right = 0;
        for (int i = 0; i < n; i++) {
            if (i < right) radius[i] = Math.Min(right - i, radius[2 * center - i]);
            while (i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n && s[i - radius[i] - 1] == s[i + radius[i] + 1])
                radius[i]++;
            if (i + radius[i] > right) { center = i; right = i + radius[i]; }
        }
        var end = new int[n];
        var start = new int[n];
        Array.Fill(end, 1);
        Array.Fill(start, 1);
        for (int i = 0; i < n; i++) {
            int r = radius[i];
            end[i + r] = Math.Max(end[i + r], 2 * r + 1);
            start[i - r] = Math.Max(start[i - r], 2 * r + 1);
        }
        for (int i = n - 2; i >= 0; i--) end[i] = Math.Max(end[i], end[i + 1] - 2);
        for (int i = 1; i < n; i++) start[i] = Math.Max(start[i], start[i - 1] - 2);
        var pre = new int[n];
        pre[0] = end[0];
        for (int i = 1; i < n; i++) pre[i] = Math.Max(pre[i - 1], end[i]);
        var suf = new int[n];
        suf[n - 1] = start[n - 1];
        for (int i = n - 2; i >= 0; i--) suf[i] = Math.Max(suf[i + 1], start[i]);
        long ans = 0;
        for (int i = 0; i < n - 1; i++) ans = Math.Max(ans, (long)pre[i] * suf[i + 1]);
        return ans;
    }
}