// LeetCode 1092 - Shortest Common Supersequence
// https://leetcode.com/problems/shortest-common-supersequence/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ShortestCommonSupersequence(string str1, string str2) {
        int m = str1.Length, n = str2.Length;
        int[,] dp = new int[m + 1, n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i, j] = dp[i - 1, j - 1] + 1;
                } else {
                    dp[i, j] = System.Math.Max(dp[i - 1, j], dp[i, j - 1]);
                }
            }
        }
        int ii = m, jj = n;
        var chars = new List<char>();
        while (ii > 0 && jj > 0) {
            if (str1[ii - 1] == str2[jj - 1]) {
                chars.Add(str1[ii - 1]);
                ii--;
                jj--;
            } else if (dp[ii - 1, jj] >= dp[ii, jj - 1]) {
                chars.Add(str1[ii - 1]);
                ii--;
            } else {
                chars.Add(str2[jj - 1]);
                jj--;
            }
        }
        while (ii > 0) {
            chars.Add(str1[--ii]);
        }
        while (jj > 0) {
            chars.Add(str2[--jj]);
        }
        chars.Reverse();
        return new string(chars.ToArray());
    }
}
