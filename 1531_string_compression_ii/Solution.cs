// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

using System;

public class Solution {
    public int GetLengthOfOptimalCompression(string s, int k) {
        int n = s.Length;
        int[,] memo = new int[n + 1, k + 1];
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= k; j++)
                memo[i, j] = -1;

        int Dp(int index, int remaining) {
            if (remaining < 0) return 1000000000;
            if (index == n || n - index <= remaining) return 0;
            if (memo[index, remaining] != -1) return memo[index, remaining];
            int answer = Dp(index + 1, remaining - 1);
            int same = 0, removed = 0;
            for (int j = index; j < n; j++) {
                if (s[j] == s[index]) {
                    same++;
                    int encoded = 1 + (same >= 2 ? 1 : 0) + (same >= 10 ? 1 : 0) + (same >= 100 ? 1 : 0);
                    answer = Math.Min(answer, encoded + Dp(j + 1, remaining - removed));
                } else {
                    removed++;
                    if (removed > remaining) break;
                }
            }
            return memo[index, remaining] = answer;
        }
        return Dp(0, k);
    }
}
