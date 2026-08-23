// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @param {number[]} source
 * @param {number[]} dest
 * @return {number}
 */
var numberOfWays = function(n, m, k, source, dest) {
    const mod = 1000000007;
    const sx = source[0], sy = source[1], tx = dest[0], ty = dest[1];
    let same = 0, row = 0, col = 0, other = 0;
    if (sx === tx && sy === ty) same = 1;
    else if (sx === tx) row = 1;
    else if (sy === ty) col = 1;
    else other = 1;
    for (let step = 0; step < k; step++) {
        const ns = (row * (m - 1) + col * (n - 1)) % mod;
        const nr = (same + (row * (m - 2)) % mod + (other * (n - 1)) % mod) % mod;
        const nc = (same + (col * (n - 2)) % mod + (other * (m - 1)) % mod) % mod;
        const no = (row * (n - 1) + col * (m - 1) + (other * (n + m - 4)) % mod) % mod;
        same = ns; row = nr; col = nc; other = no;
    }
    if (sx === tx && sy === ty) return same;
    if (sx === tx) return row;
    if (sy === ty) return col;
    return other;
};
