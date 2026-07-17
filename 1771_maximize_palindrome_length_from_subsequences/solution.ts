// LeetCode 1771 - Maximize Palindrome Length From Subsequences
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

function longestPalindrome(word1: string, word2: string): number {
    const s = word1 + word2;
    const n = s.length;
    const n1 = word1.length;
    const dp: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));
    let ans = 0;
    for (let i = n - 1; i >= 0; i--) {
        dp[i][i] = 1;
        for (let j = i + 1; j < n; j++) {
            if (s[i] === s[j]) {
                dp[i][j] = j === i + 1 ? 2 : dp[i + 1][j - 1] + 2;
                if (i < n1 && n1 <= j) {
                    ans = Math.max(ans, dp[i][j]);
                }
            } else {
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    return ans;
}
