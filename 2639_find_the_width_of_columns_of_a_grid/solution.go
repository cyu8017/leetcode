// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/


func findColumnWidth(grid [][]int) []int {
	n := len(grid[0])
	ans := make([]int, n)
	width := func(x int) int {
		if x == 0 {
			return 1
		}
		w := 0
		if x < 0 {
			w++
			x = -x
		}
		for x > 0 {
			w++
			x /= 10
		}
		return w
	}
	for _, row := range grid {
		for j, v := range row {
			w := width(v)
			if w > ans[j] {
				ans[j] = w
			}
		}
	}
	return ans
}
