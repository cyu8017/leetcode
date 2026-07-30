// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

public class Solution {
    public int NumberOfWays(int numPeople) {
        const int mod = 1_000_000_007;
        var dp = new int[numPeople + 1];
        dp[0] = 1;
        for (int people = 2; people <= numPeople; people += 2) {
            long sum = 0;
            for (int left = 0; left < people; left += 2) {
                sum = (sum + (long)dp[left] * dp[people - 2 - left]) % mod;
            }
            dp[people] = (int)sum;
        }
        return dp[numPeople];
    }
}
