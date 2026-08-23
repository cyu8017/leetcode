// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} coordinates
 * @return {number[]}
 */
var countBlackBlocks = function(m, n, coordinates) {
    const cnt = new Map();
    for (const [x, y] of coordinates) {
        for (let i = x - 1; i <= x; i++) {
            for (let j = y - 1; j <= y; j++) {
                if (i >= 0 && j >= 0 && i < m - 1 && j < n - 1) {
                    const key = i + ',' + j;
                    cnt.set(key, (cnt.get(key) || 0) + 1);
                }
            }
        }
    }
    const ans = [BigInt(m - 1) * BigInt(n - 1), 0n, 0n, 0n, 0n];
    // LeetCode expects number[]; use Number for typical constraints
    const out = Array(5).fill(0);
    out[0] = (m - 1) * (n - 1);
    for (const v of cnt.values()) {
        out[v]++;
        out[0]--;
    }
    return out;
};
