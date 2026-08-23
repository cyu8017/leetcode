// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

/**
 * @param {number[]} receiver
 * @param {number} k
 * @return {number}
 */
var getMaxFunctionValue = function(receiver, k) {
    const n = receiver.length;
    const LOG = 36;
    const up = Array.from({ length: LOG }, () => Array(n));
    const sum = Array.from({ length: LOG }, () => Array(n));
    for (let i = 0; i < n; i++) {
        up[0][i] = receiver[i];
        sum[0][i] = receiver[i];
    }
    for (let j = 1; j < LOG; j++) {
        for (let i = 0; i < n; i++) {
            const mid = up[j - 1][i];
            up[j][i] = up[j - 1][mid];
            sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
        }
    }
    let ans = 0;
    const kk0 = BigInt(k);
    for (let i = 0; i < n; i++) {
        let cur = i;
        let total = i;
        let kk = kk0;
        for (let j = 0; j < LOG; j++) {
            if ((kk & (1n << BigInt(j))) !== 0n) {
                total += sum[j][cur];
                cur = up[j][cur];
            }
        }
        if (total > ans) ans = total;
    }
    return ans;
};
