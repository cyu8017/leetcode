// LeetCode 0063 - Unique Paths II
// https://leetcode.com/problems/unique-paths-ii/

int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize) {
    if (obstacleGrid[0][0] == 1) {
        return 0;
    }

    int cols = obstacleGridColSize[0];
    int row[cols];
    for (int i = 0; i < cols; i++) {
        row[i] = 0;
    }
    row[0] = 1;

    for (int i = 0; i < obstacleGridSize; i++) {
        if (obstacleGrid[i][0] == 1) {
            row[0] = 0;
        }

        for (int j = 1; j < cols; j++) {
            if (obstacleGrid[i][j] == 1) {
                row[j] = 0;
            } else {
                row[j] += row[j - 1];
            }
        }
    }

    return row[cols - 1];
}
