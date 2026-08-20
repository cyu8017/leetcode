// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/


func firstCompleteIndex(arr []int, mat [][]int) int {
	m, n := len(mat), len(mat[0])
	pos := make([][2]int, m*n+1)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			pos[mat[i][j]] = [2]int{i, j}
		}
	}
	rowCnt := make([]int, m)
	colCnt := make([]int, n)
	for i, v := range arr {
		r, c := pos[v][0], pos[v][1]
		rowCnt[r]++
		colCnt[c]++
		if rowCnt[r] == n || colCnt[c] == m {
			return i
		}
	}
	return -1
}
