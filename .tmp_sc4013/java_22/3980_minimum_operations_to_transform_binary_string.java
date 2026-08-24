// CONFIG class=Solution method=minOperations types=None
// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

class Solution {
    public int minOperations(String s1, String s2) {
        final int infinity = 1000000000;
        int[] dp = new int[] { 0, infinity };
        int n = s1.length();
        for (int i = 0; i < n; i++) {
            int[] next = new int[] { infinity, infinity };
            for (int forcedZero = 0; forcedZero <= 1; forcedZero++) {
                if (dp[forcedZero] == infinity) continue;
                char current = s1.charAt(i);
                if (forcedZero == 1) current = '0';
                int direct = dp[forcedZero];
                if (current == '0' && s2.charAt(i) == '1') direct++;
                else if (current == '1' && s2.charAt(i) == '0') direct = infinity;
                next[0] = Math.min(next[0], direct);
                if (i + 1 < n) {
                    int cost = dp[forcedZero] + 1;
                    if (current == '0') cost++;
                    if (s1.charAt(i + 1) == '0') cost++;
                    if (s2.charAt(i) == '1') cost++;
                    next[1] = Math.min(next[1], cost);
                }
            }
            dp = next;
        }
        return dp[0] == infinity ? -1 : dp[0];
    }
}
