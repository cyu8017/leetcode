// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

class Solution {
    public int numberOfWays(int numPeople) {
        int mod = 1_000_000_007;
        int[] dp = new int[numPeople + 1];
        dp[0] = 1;
        for (int people = 2; people <= numPeople; people += 2) {
            long ways = 0;
            for (int left = 0; left < people; left += 2) {
                ways = (ways + (long) dp[left] * dp[people - 2 - left]) % mod;
            }
            dp[people] = (int) ways;
        }
        return dp[numPeople];
    }
}

