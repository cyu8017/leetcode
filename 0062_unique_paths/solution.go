// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

func uniquePaths(m int, n int) int {
	row := make([]int, n)
	for i := range row {
		row[i] = 1
	}

	for r := 1; r < m; r++ {
		for col := 1; col < n; col++ {
			row[col] += row[col-1]
		}
	}

	return row[n-1]
}
