// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

var findColumnWidth = function(grid) {
    const n = grid[0].length;
    const ans = new Array(n).fill(0);
    const width = (x) => {
        if (x === 0) return 1;
        let w = 0;
        if (x < 0) { w++; x = -x; }
        while (x > 0) { w++; x = Math.floor(x / 10); }
        return w;
    };
    for (const row of grid) {
        for (let j = 0; j < n; j++) ans[j] = Math.max(ans[j], width(row[j]));
    }
    return ans;
};
