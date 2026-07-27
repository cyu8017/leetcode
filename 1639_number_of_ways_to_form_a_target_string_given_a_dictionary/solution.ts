// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

function numWays(words: string[], target: string): number {
    const MOD = 1000000007;
    const m = words[0].length;
    const dp = Array(target.length + 1).fill(0);
    dp[0] = 1;
    for (let j = 0; j < m; j++) {
        const count = Array(26).fill(0);
        for (const word of words) count[word.charCodeAt(j) - 97]++;
        for (let i = Math.min(j + 1, target.length); i > 0; i--) {
            dp[i] = (dp[i] + dp[i - 1] * count[target.charCodeAt(i - 1) - 97]) % MOD;
        }
    }
    return dp[target.length];
}
