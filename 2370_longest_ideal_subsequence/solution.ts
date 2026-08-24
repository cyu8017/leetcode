// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

export function longestIdealString(s: string, k: number): number {
    const dp = Array(26).fill(0);
    let ans = 0;
    for (const ch of s) {
        const c = ch.charCodeAt(0) - 97;
        let best = 0;
        for (let p = 0; p < 26; p++)
            if (Math.abs(c - p) <= k && dp[p] > best) best = dp[p];
        dp[c] = best + 1;
        ans = Math.max(ans, dp[c]);
    }
    return ans;
}
