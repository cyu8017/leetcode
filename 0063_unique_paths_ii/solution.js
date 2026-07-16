// LeetCode 0063 - Unique Paths II
// https://leetcode.com/problems/unique-paths-ii/

/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    if (obstacleGrid[0][0] === 1) {
        return 0;
    }

    const rows = obstacleGrid.length;
    const cols = obstacleGrid[0].length;
    const row = new Array(cols).fill(0);
    row[0] = 1;

    for (let i = 0; i < rows; i++) {
        if (obstacleGrid[i][0] === 1) {
            row[0] = 0;
        }

        for (let j = 1; j < cols; j++) {
            if (obstacleGrid[i][j] === 1) {
                row[j] = 0;
            } else {
                row[j] += row[j - 1];
            }
        }
    }

    return row[cols - 1];
};
