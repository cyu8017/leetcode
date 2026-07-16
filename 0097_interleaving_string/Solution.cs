// LeetCode 0097 - Interleaving String
// https://leetcode.com/problems/interleaving-string/

public class Solution {
    public bool IsInterleave(string s1, string s2, string s3) {
        if (s1.Length + s2.Length != s3.Length) {
            return false;
        }

        int m = s1.Length;
        int n = s2.Length;
        bool[] dp = new bool[n + 1];
        dp[0] = true;

        for (int j = 1; j <= n; j++) {
            dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1];
        }

        for (int i = 1; i <= m; i++) {
            dp[0] = dp[0] && s1[i - 1] == s3[i - 1];
            for (int j = 1; j <= n; j++) {
                dp[j] = (dp[j] && s1[i - 1] == s3[i + j - 1])
                        || (dp[j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }

        return dp[n];
    }
}
