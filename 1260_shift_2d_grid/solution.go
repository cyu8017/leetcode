// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

func shiftGrid(grid [][]int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	flat := make([]int, 0, m*n)
	for _, row := range grid {
		flat = append(flat, row...)
	}
	k %= len(flat)
	if k > 0 {
		flat = append(flat[len(flat)-k:], flat[:len(flat)-k]...)
	}
	ans := make([][]int, m)
	for i := 0; i < m; i++ {
		ans[i] = flat[i*n : (i+1)*n]
	}
	return ans
}
