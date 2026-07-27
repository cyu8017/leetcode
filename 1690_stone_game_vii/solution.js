// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

/**
 * @param {number[]} stones
 * @return {number}
 */
var stoneGameVII = function(stones) {
    const n = stones.length;
    const pre = [0];
    for (const x of stones) pre.push(pre[pre.length - 1] + x);
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    for (let length = 2; length <= n; length++) {
        for (let i = 0; i <= n - length; i++) {
            const j = i + length - 1;
            dp[i][j] = Math.max(pre[j + 1] - pre[i + 1] - dp[i + 1][j], pre[j] - pre[i] - dp[i][j - 1]);
        }
    }
    return dp[0][n - 1];
};
