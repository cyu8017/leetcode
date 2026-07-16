// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

public class Solution {
    public int FindMaxForm(string[] strs, int m, int n) {
        int[,] dp = new int[m + 1, n + 1];
        foreach (string str in strs) {
            int zeros = str.Count(ch => ch == '0');
            int ones = str.Length - zeros;
            for (int zero = m; zero >= zeros; zero--) {
                for (int one = n; one >= ones; one--) {
                    dp[zero, one] = Math.Max(dp[zero, one], dp[zero - zeros, one - ones] + 1);
                }
            }
        }
        return dp[m, n];
    }
}
