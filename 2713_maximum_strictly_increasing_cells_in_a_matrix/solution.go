// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/


import "sort"

func maxIncreasingCells(mat [][]int) int {
	m, n := len(mat), len(mat[0])
	type cell struct{ v, r, c int }
	cells := make([]cell, 0, m*n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			cells = append(cells, cell{mat[i][j], i, j})
		}
	}
	sort.Slice(cells, func(i, j int) bool { return cells[i].v < cells[j].v })
	rowMax := make([]int, m)
	colMax := make([]int, n)
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	ans := 0
	for i := 0; i < len(cells); {
		j := i
		for j < len(cells) && cells[j].v == cells[i].v {
			j++
		}
		type upd struct{ r, c, val int }
		buf := []upd{}
		for k := i; k < j; k++ {
			r, c := cells[k].r, cells[k].c
			best := rowMax[r]
			if colMax[c] > best {
				best = colMax[c]
			}
			dp[r][c] = best + 1
			if dp[r][c] > ans {
				ans = dp[r][c]
			}
			buf = append(buf, upd{r, c, dp[r][c]})
		}
		for _, u := range buf {
			if u.val > rowMax[u.r] {
				rowMax[u.r] = u.val
			}
			if u.val > colMax[u.c] {
				colMax[u.c] = u.val
			}
		}
		i = j
	}
	return ans
}
