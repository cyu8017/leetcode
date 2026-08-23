// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minTotalDistance = function(grid) {
    const rows = [];
    const cols = [];
    for (let rowIndex = 0; rowIndex < grid.length; rowIndex += 1) {
        for (let colIndex = 0; colIndex < grid[0].length; colIndex += 1) {
            if (grid[rowIndex][colIndex] === 1) {
                rows.push(rowIndex);
                cols.push(colIndex);
            }
        }
    }
    cols.sort((a, b) => a - b);
    const rowMedian = rows[Math.floor(rows.length / 2)];
    const colMedian = cols[Math.floor(cols.length / 2)];
    return rows.reduce((sum, row) => sum + Math.abs(row - rowMedian), 0)
        + cols.reduce((sum, col) => sum + Math.abs(col - colMedian), 0);
};
