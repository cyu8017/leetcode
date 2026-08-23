// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var superEggDrop = function(k, n) {
    const dp = new Array(k + 1).fill(0);
    let moves = 0;
    while (dp[k] < n) {
        moves++;
        for (let eggs = k; eggs >= 1; eggs--) {
            dp[eggs] = dp[eggs] + dp[eggs - 1] + 1;
        }
    }
    return moves;
};
