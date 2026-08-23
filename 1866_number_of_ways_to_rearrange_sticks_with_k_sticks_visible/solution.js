// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var rearrangeSticks = function(n, k) {
    const mod = 1e9 + 7;
    if (k === 0 || k > n) return 0;
    const dp = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    dp[1][1] = 1;
    for (let sticks = 2; sticks <= n; sticks++) {
        dp[sticks][1] = ((sticks - 1) * dp[sticks - 1][1]) % mod;
        for (let visible = 2; visible <= sticks; visible++) {
            dp[sticks][visible] = (dp[sticks - 1][visible - 1] + (sticks - 1) * dp[sticks - 1][visible]) % mod;
        }
    }
    return dp[n][k];
};
