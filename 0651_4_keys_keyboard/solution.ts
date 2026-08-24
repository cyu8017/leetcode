// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

export function maxA(n: number): number {
    const dp = Array(n + 1).fill(0);
    for (let i = 0; i <= n; ++i) dp[i] = i;
    for (let i = 1; i <= n; ++i) {
        for (let j = 0; j < i - 2; ++j) {
            dp[i] = Math.max(dp[i], dp[j] * (i - j - 1));
        }
    }
    return dp[n];
}
