// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

func largestLocal(grid [][]int) [][]int {
	n := len(grid)
	ans := make([][]int, n-2)
	for i := 0; i < n-2; i++ {
		ans[i] = make([]int, n-2)
		for j := 0; j < n-2; j++ {
			mx := 0
			for r := i; r < i+3; r++ {
				for c := j; c < j+3; c++ {
					if grid[r][c] > mx {
						mx = grid[r][c]
					}
				}
			}
			ans[i][j] = mx
		}
	}
	return ans
}
