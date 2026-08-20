// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

func rangeAddQueries(n int, queries [][]int) [][]int {
	diff := make([][]int, n+1)
	for i := range diff {
		diff[i] = make([]int, n+1)
	}
	for _, q := range queries {
		r1, c1, r2, c2 := q[0], q[1], q[2], q[3]
		diff[r1][c1]++
		diff[r1][c2+1]--
		diff[r2+1][c1]--
		diff[r2+1][c2+1]++
	}
	mat := make([][]int, n)
	for i := 0; i < n; i++ {
		mat[i] = make([]int, n)
		for j := 0; j < n; j++ {
			v := diff[i][j]
			if i > 0 {
				v += mat[i-1][j]
			}
			if j > 0 {
				v += mat[i][j-1]
			}
			if i > 0 && j > 0 {
				v -= mat[i-1][j-1]
			}
			mat[i][j] = v
		}
	}
	return mat
}
