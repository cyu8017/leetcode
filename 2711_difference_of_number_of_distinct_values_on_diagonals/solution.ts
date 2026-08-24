// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

export function differenceOfDistinctValues(grid: any): any {
    const m = grid.length, n = grid[0].length;
    const ans = Array.from({ length: m }, () => new Array(n));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const top = new Set(), bot = new Set();
            for (let r = i - 1, c = j - 1; r >= 0 && c >= 0; r--, c--) top.add(grid[r][c]);
            for (let r = i + 1, c = j + 1; r < m && c < n; r++, c++) bot.add(grid[r][c]);
            ans[i][j] = Math.abs(top.size - bot.size);
        }
    }
    return ans;
}
