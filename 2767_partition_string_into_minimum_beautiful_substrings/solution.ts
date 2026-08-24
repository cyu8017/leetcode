// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

export function minimumBeautifulSubstrings(s: string): number {
    const n = s.length;
    const pow5 = new Set();
    for (let x = 1n; ; x *= 5n) {
        const b = x.toString(2);
        if (b.length > n) break;
        pow5.add(b);
    }
    const INF = 1e9;
    const dp = Array(n + 1).fill(INF);
    dp[0] = 0;
    for (let i = 0; i < n; i++) {
        if (dp[i] === INF || s[i] === '0') continue;
        for (let j = i + 1; j <= n; j++) {
            if (pow5.has(s.slice(i, j))) dp[j] = Math.min(dp[j], dp[i] + 1);
        }
    }
    return dp[n] === INF ? -1 : dp[n];
}
