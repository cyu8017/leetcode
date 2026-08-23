// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

/**
 * @param {string} s
 * @return {number}
 */
var numPermsDISequence = function(s) {
    const MOD = 1000000007;
    const n = s.length;
    let dp = new Array(n + 1).fill(1);
    for (let i = 1; i <= n; i++) {
        const newDp = new Array(n + 1).fill(0);
        if (s[i - 1] === "I") {
            let postfix = 0;
            for (let j = n - i; j >= 0; j--) {
                postfix = (postfix + dp[j + 1]) % MOD;
                newDp[j] = postfix;
            }
        } else {
            let prefix = 0;
            for (let j = 0; j <= n - i; j++) {
                prefix = (prefix + dp[j]) % MOD;
                newDp[j] = prefix;
            }
        }
        dp = newDp;
    }
    return dp[0];
};
