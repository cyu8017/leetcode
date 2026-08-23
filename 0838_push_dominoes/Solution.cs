// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

using System;
using System.Text;

public class Solution {
    public string PushDominoes(string dominoes) {
        int n = dominoes.Length;
        int[] force = new int[n];
        int f = 0;
        for (int i = 0; i < n; i++) {
            if (dominoes[i] == 'R') f = n;
            else if (dominoes[i] == 'L') f = 0;
            else f = Math.Max(f - 1, 0);
            force[i] += f;
        }
        f = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (dominoes[i] == 'L') f = n;
            else if (dominoes[i] == 'R') f = 0;
            else f = Math.Max(f - 1, 0);
            force[i] -= f;
        }
        var sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            if (force[i] > 0) sb.Append('R');
            else if (force[i] < 0) sb.Append('L');
            else sb.Append('.');
        }
        return sb.ToString();
    }
}
