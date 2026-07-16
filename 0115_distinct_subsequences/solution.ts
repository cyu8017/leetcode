// LeetCode 0115 - Distinct Subsequences
// https://leetcode.com/problems/distinct-subsequences/

export function numDistinct(s: string, t: string): number {
    const dp: number[] = new Array(t.length + 1).fill(0);
    dp[0] = 1;

    for (const char of s) {
        for (let index = t.length - 1; index >= 0; index--) {
            if (char === t[index]) {
                dp[index + 1] += dp[index];
            }
        }
    }

    return dp[t.length];
}