// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

/**
 * @param {number[][]} matrix
 * @param {number} numSelect
 * @return {number}
 */
var maximumRows = function(matrix, numSelect) {
    const m = matrix.length, n = matrix[0].length;
    let ans = 0;
    const dfs = (col, chosen, mask) => {
        if (chosen === numSelect) {
            let covered = 0;
            for (let i = 0; i < m; i++) {
                let ok = true;
                for (let j = 0; j < n; j++) {
                    if (matrix[i][j] === 1 && ((mask >> j) & 1) === 0) {
                        ok = false;
                        break;
                    }
                }
                if (ok) covered++;
            }
            ans = Math.max(ans, covered);
            return;
        }
        if (col === n) return;
        dfs(col + 1, chosen + 1, mask | (1 << col));
        dfs(col + 1, chosen, mask);
    };
    dfs(0, 0, 0);
    return ans;
};
