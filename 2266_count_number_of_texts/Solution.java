// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

class Solution {
    public int countTexts(String pressedKeys) {
        final int mod = 1000000007;
        int n = pressedKeys.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1];
            int maxPress = (pressedKeys.charAt(i - 1) == '7' || pressedKeys.charAt(i - 1) == '9') ? 4 : 3;
            for (int j = 2; j <= maxPress && j <= i; j++) {
                if (pressedKeys.charAt(i - j) != pressedKeys.charAt(i - 1)) break;
                dp[i] = (dp[i] + dp[i - j]) % mod;
            }
        }
        return dp[n];
    }
}
