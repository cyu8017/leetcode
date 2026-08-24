// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

export function countTexts(pressedKeys: string): number {
    const mod = 1000000007;
    const n = pressedKeys.length;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (let i = 1; i <= n; i++) {
        dp[i] = dp[i - 1];
        const maxPress = (pressedKeys[i - 1] === '7' || pressedKeys[i - 1] === '9') ? 4 : 3;
        for (let j = 2; j <= maxPress && j <= i; j++) {
            if (pressedKeys[i - j] !== pressedKeys[i - 1]) break;
            dp[i] = (dp[i] + dp[i - j]) % mod;
        }
    }
    return dp[n];
}
