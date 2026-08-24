// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var constructProductMatrix = function(grid) {
    const mod = 12345;
    const m = grid.length, n = grid[0].length;
    const ans = Array.from({ length: m }, () => Array(n));
    let pref = 1;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) {
            ans[i][j] = pref;
            pref = (pref * (grid[i][j] % mod)) % mod;
        }
    let suf = 1;
    for (let i = m - 1; i >= 0; i--)
        for (let j = n - 1; j >= 0; j--) {
            ans[i][j] = (ans[i][j] * suf) % mod;
            suf = (suf * (grid[i][j] % mod)) % mod;
        }
    return ans;
};
