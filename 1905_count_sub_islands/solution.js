// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

/**
 * @param {number[][]} grid1
 * @param {number[][]} grid2
 * @return {number}
 */
var countSubIslands = function(grid1, grid2) {
    const rows = grid2.length, cols = grid2[0].length;
    const dfs = (r, c) => {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] === 0) return true;
        grid2[r][c] = 0;
        let ok = grid1[r][c] === 1;
        for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
            if (!dfs(nr, nc)) ok = false;
        }
        return ok;
    };
    let ans = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid2[r][c] === 1 && dfs(r, c)) ans++;
        }
    }
    return ans;
};
