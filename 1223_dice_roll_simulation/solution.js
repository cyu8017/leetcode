// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

/**
 * @param {number} n
 * @param {number[]} rollMax
 * @return {number}
 */
var dieSimulator = function(n, rollMax) {
    const mod = 1000000007;
    let dp = rollMax.map((limit) => Array(limit + 1).fill(0));
    for (let j = 0; j < 6; j++) dp[j][1] = 1;
    for (let t = 1; t < n; t++) {
        const totals = dp.map((row) => row.reduce((s, v) => (s + v) % mod, 0));
        const nxt = rollMax.map((limit) => Array(limit + 1).fill(0));
        for (let j = 0; j < 6; j++) {
            nxt[j][1] = (totals.reduce((s, v) => (s + v) % mod, 0) - totals[j] + mod) % mod;
            for (let run = 2; run < dp[j].length; run++) {
                nxt[j][run] = dp[j][run - 1];
            }
        }
        dp = nxt;
    }
    return dp.reduce((s, row) => (s + row.reduce((a, b) => (a + b) % mod, 0)) % mod, 0);
};
