// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

export function goodBinaryStrings(minLength: number, maxLength: number, oneGroup: number, zeroGroup: number): number {
    const MOD = 1000000007;
    const dp = new Array(maxLength + 1).fill(0);
    dp[0] = 1;
    for (let i = 0; i <= maxLength; i++) {
        if (dp[i] === 0) continue;
        if (i + oneGroup <= maxLength) dp[i + oneGroup] = (dp[i + oneGroup] + dp[i]) % MOD;
        if (i + zeroGroup <= maxLength) dp[i + zeroGroup] = (dp[i + zeroGroup] + dp[i]) % MOD;
    }
    let ans = 0;
    for (let i = minLength; i <= maxLength; i++) ans = (ans + dp[i]) % MOD;
    return ans;
}
