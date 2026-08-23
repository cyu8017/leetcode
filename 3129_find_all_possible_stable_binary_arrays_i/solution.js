// LeetCode 3129 - Find All Possible Stable Binary Arrays I
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

/**
 * @param {number} zero
 * @param {number} one
 * @param {number} limit
 * @return {number}
 */
var numberOfStableArrays = function(zero, one, limit) {
    const MOD = 1000000007;
    const f = Array.from({ length: zero + 1 }, () =>
        Array.from({ length: one + 1 }, () => [-1, -1]));
    const dfs = (i, j, k) => {
        if (i < 0 || j < 0) return 0;
        if (i === 0) return (k === 1 && j <= limit) ? 1 : 0;
        if (j === 0) return (k === 0 && i <= limit) ? 1 : 0;
        if (f[i][j][k] !== -1) return f[i][j][k];
        let res;
        if (k === 0)
            res = (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD;
        else
            res = (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD;
        return f[i][j][k] = res;
    };
    return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD;
};
