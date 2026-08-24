// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

export function idealArrays(n: number, maxValue: number): number {
    const mod = 1000000007;
    const maxLen = 14;
    const comb = Array.from({ length: n + 1 }, () => Array(maxLen + 1).fill(0));
    for (let i = 0; i <= n; i++) {
        comb[i][0] = 1;
        for (let j = 1; j <= maxLen && j <= i; j++)
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod;
    }
    const dp = Array.from({ length: maxValue + 1 }, () => Array(maxLen + 1).fill(0));
    for (let i = 1; i <= maxValue; i++) dp[i][1] = 1;
    for (let len = 2; len <= maxLen; len++) {
        for (let v = 1; v <= maxValue; v++) {
            for (let m = 2 * v; m <= maxValue; m += v)
                dp[m][len] = (dp[m][len] + dp[v][len - 1]) % mod;
        }
    }
    let ans = 0;
    for (let v = 1; v <= maxValue; v++) {
        for (let len = 1; len <= maxLen && len <= n; len++)
            ans = (ans + (dp[v][len] * comb[n - 1][len - 1]) % mod) % mod;
    }
    return ans;
}
