// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function(n, k, target) {
    const MOD = 1e9 + 7;
    let dp = Array(target + 1).fill(0);
    dp[0] = 1;
    for (let dice = 0; dice < n; dice++) {
        const next = Array(target + 1).fill(0);
        for (let s = 0; s <= target; s++) {
            if (!dp[s]) continue;
            for (let face = 1; face <= k; face++) {
                if (s + face <= target) next[s + face] = (next[s + face] + dp[s]) % MOD;
            }
        }
        dp = next;
    }
    return dp[target];
};
