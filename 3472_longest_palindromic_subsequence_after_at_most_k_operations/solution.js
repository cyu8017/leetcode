// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

var longestPalindromicSubsequence = function(s, k) {
    const n = s.length;
    const dp = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => new Array(k + 1).fill(-1))
    );
    const distCirc = (a, b) => {
        const d = Math.abs(a.charCodeAt(0) - b.charCodeAt(0));
        return Math.min(d, 26 - d);
    };
    const dfs = (i, j, ops) => {
        if (i > j) return 0;
        if (i === j) return 1;
        if (dp[i][j][ops] !== -1) return dp[i][j][ops];
        let best = dfs(i + 1, j, ops);
        best = Math.max(best, dfs(i, j - 1, ops));
        const cost = distCirc(s[i], s[j]);
        if (cost <= ops) best = Math.max(best, 2 + dfs(i + 1, j - 1, ops - cost));
        return (dp[i][j][ops] = best);
    };
    return dfs(0, n - 1, k);
};
