// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

/**
 * @param {number[]} prob
 * @param {number} target
 * @return {number}
 */
var probabilityOfHeads = function(prob, target) {
    const dp = Array(target + 1).fill(0);
    dp[0] = 1;
    for (const p of prob) {
        for (let heads = target; heads >= 0; heads--) {
            dp[heads] = dp[heads] * (1 - p) + (heads ? dp[heads - 1] * p : 0);
        }
    }
    return dp[target];
};
