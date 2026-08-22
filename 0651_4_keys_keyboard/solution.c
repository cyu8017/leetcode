// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

int maxA(int n) {
    int dp[51];
    for (int i = 0; i <= n; i++) {
        dp[i] = i;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i - 1; j++) {
            int candidate = dp[j] * (i - j - 1);
            if (candidate > dp[i]) {
                dp[i] = candidate;
            }
        }
    }
    return dp[n];
}
