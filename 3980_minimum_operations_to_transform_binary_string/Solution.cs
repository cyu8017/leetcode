// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

using System;

public class Solution {
    public int MinOperations(string s1, string s2) {
        const int infinity = 1000000000;
        int[] dp = new int[] { 0, infinity };
        int n = s1.Length;
        for (int i = 0; i < n; i++) {
            int[] next = new int[] { infinity, infinity };
            for (int forcedZero = 0; forcedZero <= 1; forcedZero++) {
                if (dp[forcedZero] == infinity) continue;
                char current = s1[i];
                if (forcedZero == 1) current = '0';
                int direct = dp[forcedZero];
                if (current == '0' && s2[i] == '1') direct++;
                else if (current == '1' && s2[i] == '0') direct = infinity;
                next[0] = Math.Min(next[0], direct);
                if (i + 1 < n) {
                    int cost = dp[forcedZero] + 1;
                    if (current == '0') cost++;
                    if (s1[i + 1] == '0') cost++;
                    if (s2[i] == '1') cost++;
                    next[1] = Math.Min(next[1], cost);
                }
            }
            dp = next;
        }
        return dp[0] == infinity ? -1 : dp[0];
    }
}
