// LeetCode 0063 - Unique Paths II
// https://leetcode.com/problems/unique-paths-ii/

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if obstacleGrid[0][0] == 1 {
		return 0
	}

	rows := len(obstacleGrid)
	cols := len(obstacleGrid[0])
	row := make([]int, cols)
	row[0] = 1

	for i := 0; i < rows; i++ {
		if obstacleGrid[i][0] == 1 {
			row[0] = 0
		}

		for j := 1; j < cols; j++ {
			if obstacleGrid[i][j] == 1 {
				row[j] = 0
			} else {
				row[j] += row[j-1]
			}
		}
	}

	return row[cols-1]
}
