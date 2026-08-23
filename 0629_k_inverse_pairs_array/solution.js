// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kInversePairs = function(n, k) {
    const mod = 1000000007;
    let dp = Array(k + 1).fill(0);
    dp[0] = 1;
    for (let size = 1; size <= n; ++size) {
        const nxt = Array(k + 1).fill(0);
        let prefix = 0;
        for (let pairs = 0; pairs <= k; ++pairs) {
            prefix = (prefix + dp[pairs]) % mod;
            if (pairs >= size) prefix = (prefix - dp[pairs - size] + mod) % mod;
            nxt[pairs] = prefix;
        }
        dp = nxt;
    }
    return dp[k];
};
