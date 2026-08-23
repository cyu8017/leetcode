// LeetCode 0063 - Unique Paths II
// https://leetcode.com/problems/unique-paths-ii/

public class Solution {
    public int UniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }

        int rows = obstacleGrid.Length;
        int cols = obstacleGrid[0].Length;
        int[] row = new int[cols];
        row[0] = 1;

        for (int i = 0; i < rows; i++) {
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
}
