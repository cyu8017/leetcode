// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

func oddCells(m int, n int, indices [][]int) int {
	rows := make([]int, m)
	cols := make([]int, n)
	for _, idx := range indices {
		rows[idx[0]] ^= 1
		cols[idx[1]] ^= 1
	}
	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			ans += rows[r] ^ cols[c]
		}
	}
	return ans
}
