// LeetCode 1582 - Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

func numSpecial(mat [][]int) int {
	m, n := len(mat), len(mat[0])
	rows := make([]int, m)
	cols := make([]int, n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			rows[i] += mat[i][j]
			cols[j] += mat[i][j]
		}
	}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] == 1 && rows[i] == 1 && cols[j] == 1 {
				ans++
			}
		}
	}
	return ans
}
