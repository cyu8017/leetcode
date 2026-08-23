// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

/**
 * @param {number[]} coins
 * @param {number} maxJump
 * @return {number[]}
 */
var cheapestJump = function(coins, maxJump) {
    const n = coins.length;
    if (coins[n - 1] === -1) return [];
    const inf = Number.MAX_SAFE_INTEGER / 4;
    const cost = Array(n).fill(inf);
    const nxt = Array(n).fill(-1);
    cost[n - 1] = coins[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        if (coins[i] === -1) continue;
        for (let jump = 1; jump <= maxJump; ++jump) {
            const j = i + jump;
            if (j >= n) break;
            if (cost[j] === inf) continue;
            const candidate = coins[i] + cost[j];
            if (candidate < cost[i] || (candidate === cost[i] && (nxt[i] === -1 || j < nxt[i]))) {
                cost[i] = candidate;
                nxt[i] = j;
            }
        }
    }
    if (cost[0] === inf) return [];
    const path = [1];
    let i = 0;
    while (i !== n - 1) {
        i = nxt[i];
        path.push(i + 1);
    }
    return path;
};
