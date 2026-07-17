// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

func findBall(grid [][]int) []int {
	m, n := len(grid), len(grid[0])
	ans := make([]int, n)
	for start := 0; start < n; start++ {
		col := start
		for row := 0; row < m; row++ {
			next := col + grid[row][col]
			if next < 0 || next == n || grid[row][next] != grid[row][col] {
				col = -1
				break
			}
			col = next
		}
		ans[start] = col
	}
	return ans
}
