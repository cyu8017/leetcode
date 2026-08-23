// LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var isPossibleToCutPath = function(grid) {
    const m = grid.length, n = grid[0].length;
    const dfs = (r, c) => {
        if (r === m - 1 && c === n - 1) return true;
        if (r >= m || c >= n || grid[r][c] === 0) return false;
        if (!(r === 0 && c === 0)) grid[r][c] = 0;
        return dfs(r + 1, c) || dfs(r, c + 1);
    };
    if (!dfs(0, 0)) return true;
    grid[0][0] = 1;
    return !dfs(0, 0);
};
