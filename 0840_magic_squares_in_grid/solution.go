// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

import "sort"

func numMagicSquaresInside(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	if rows < 3 || cols < 3 {
		return 0
	}
	magic := func(r, c int) bool {
		vals := make([]int, 0, 9)
		for i := 0; i < 3; i++ {
			for j := 0; j < 3; j++ {
				vals = append(vals, grid[r+i][c+j])
			}
		}
		sorted := append([]int{}, vals...)
		sort.Ints(sorted)
		for i := 0; i < 9; i++ {
			if sorted[i] != i+1 {
				return false
			}
		}
		a := grid
		return a[r][c]+a[r][c+1]+a[r][c+2] == 15 &&
			a[r+1][c]+a[r+1][c+1]+a[r+1][c+2] == 15 &&
			a[r+2][c]+a[r+2][c+1]+a[r+2][c+2] == 15 &&
			a[r][c]+a[r+1][c]+a[r+2][c] == 15 &&
			a[r][c+1]+a[r+1][c+1]+a[r+2][c+1] == 15 &&
			a[r][c+2]+a[r+1][c+2]+a[r+2][c+2] == 15 &&
			a[r][c]+a[r+1][c+1]+a[r+2][c+2] == 15 &&
			a[r][c+2]+a[r+1][c+1]+a[r+2][c] == 15
	}
	ans := 0
	for i := 0; i < rows-2; i++ {
		for j := 0; j < cols-2; j++ {
			if magic(i, j) {
				ans++
			}
		}
	}
	return ans
}
