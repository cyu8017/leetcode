// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

var minimumArea = function(grid) {
    let x1 = grid.length, y1 = grid[0].length, x2 = 0, y2 = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === 1) {
                x1 = Math.min(x1, i); y1 = Math.min(y1, j);
                x2 = Math.max(x2, i); y2 = Math.max(y2, j);
            }
        }
    }
    return (x2 - x1 + 1) * (y2 - y1 + 1);
};
