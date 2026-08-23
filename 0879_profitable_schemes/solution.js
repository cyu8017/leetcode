// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

/**
 * @param {number} n
 * @param {number} minProfit
 * @param {number[]} group
 * @param {number[]} profit
 * @return {number}
 */
var profitableSchemes = function(n, minProfit, group, profit) {
    const MOD = 1000000007;
    const dp = Array.from({ length: n + 1 }, () => new Array(minProfit + 1).fill(0));
    dp[0][0] = 1;
    for (let i = 0; i < group.length; i++) {
        const members = group[i], p = profit[i];
        for (let people = n; people >= members; people--) {
            for (let prof = minProfit; prof >= 0; prof--) {
                const np = Math.min(minProfit, prof + p);
                dp[people][np] = (dp[people][np] + dp[people - members][prof]) % MOD;
            }
        }
    }
    let ans = 0;
    for (let people = 0; people <= n; people++) ans = (ans + dp[people][minProfit]) % MOD;
    return ans;
};
