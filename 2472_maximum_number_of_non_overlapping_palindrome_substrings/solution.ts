// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

export function maxPalindromes(s: string, k: number): number {
    const n = s.length;
    const isPal = Array.from({ length: n }, () => Array(n).fill(false));
    for (let i = 0; i < n; i++) isPal[i][i] = true;
    for (let i = 0; i + 1 < n; i++) isPal[i][i + 1] = s[i] === s[i + 1];
    for (let length = 3; length <= n; length++) {
        for (let i = 0; i + length - 1 < n; i++) {
            const j = i + length - 1;
            isPal[i][j] = s[i] === s[j] && isPal[i + 1][j - 1];
        }
    }
    const dp = Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        dp[i] = dp[i + 1];
        for (let j = i + k - 1; j < n; j++) {
            if (isPal[i][j] && 1 + dp[j + 1] > dp[i]) dp[i] = 1 + dp[j + 1];
        }
    }
    return dp[0];
}
