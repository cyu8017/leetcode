// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

export function minExtraChar(s: any, dictionary: any): any {
    const dict = new Set(dictionary);
    const n = s.length;
    const dp = new Array(n + 1).fill(n);
    dp[0] = 0;
    for (let i = 0; i < n; i++) {
        dp[i + 1] = Math.min(dp[i + 1], dp[i] + 1);
        for (let j = i + 1; j <= n; j++) {
            if (dict.has(s.slice(i, j))) dp[j] = Math.min(dp[j], dp[i]);
        }
    }
    return dp[n];
}
