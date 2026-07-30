// LeetCode 1444 - Number Of Ways Of Cutting A Pizza
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

using System.Collections.Generic;
public class Solution {
    public int Ways(string[] pizza, int k) {
        int mod = 1000000007, rows = pizza.Length, cols = pizza[0].Length;
        var apples = new int[rows + 1, cols + 1];
        for (int r = rows - 1; r >= 0; r--)
            for (int c = cols - 1; c >= 0; c--)
                apples[r, c] = (pizza[r][c] == 'A' ? 1 : 0) + apples[r + 1, c] + apples[r, c + 1] - apples[r + 1, c + 1];
        var dp = new int[rows, cols];
        for (int r = 0; r < rows; r++) for (int c = 0; c < cols; c++) dp[r, c] = apples[r, c] > 0 ? 1 : 0;
        for (int cut = 1; cut < k; cut++) {
            var nxt = new int[rows, cols];
            for (int r = 0; r < rows; r++)
                for (int c = 0; c < cols; c++) {
                    for (int nr = r + 1; nr < rows; nr++)
                        if (apples[r, c] > apples[nr, c]) nxt[r, c] = (nxt[r, c] + dp[nr, c]) % mod;
                    for (int nc = c + 1; nc < cols; nc++)
                        if (apples[r, c] > apples[r, nc]) nxt[r, c] = (nxt[r, c] + dp[r, nc]) % mod;
                }
            dp = nxt;
        }
        return dp[0, 0];
    }
}
