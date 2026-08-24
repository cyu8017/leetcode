// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

export function countGoodStrings(low: number, high: number, zero: number, one: number): number {
    const mod = 1000000007;
    const dp = Array(high + 1).fill(0);
    dp[0] = 1;
    let ans = 0;
    for (let i = 1; i <= high; i++) {
        if (i >= zero) dp[i] = (dp[i] + dp[i - zero]) % mod;
        if (i >= one) dp[i] = (dp[i] + dp[i - one]) % mod;
        if (i >= low) ans = (ans + dp[i]) % mod;
    }
    return ans;
}
