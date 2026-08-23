// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

using System;

public class Solution {
    public int MinOperations(string word1, string word2) {
        int n = word1.Length;
        int[] f = new int[n + 1];
        for (int i = 0; i <= n; i++) f[i] = int.MaxValue / 2;
        f[0] = 0;
        int Calc(int l, int r, bool rev) {
            int[,] cnt = new int[26, 26];
            int res = 0;
            for (int i = l; i <= r; i++) {
                int j = rev ? r - (i - l) : i;
                int a = word1[j] - 'a';
                int b = word2[i] - 'a';
                if (a != b) {
                    if (cnt[b, a] > 0) cnt[b, a]--;
                    else { cnt[a, b]++; res++; }
                }
            }
            return res;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int a = Calc(j, i - 1, false);
                int b = 1 + Calc(j, i - 1, true);
                f[i] = Math.Min(f[i], f[j] + Math.Min(a, b));
            }
        }
        return f[n];
    }
}
