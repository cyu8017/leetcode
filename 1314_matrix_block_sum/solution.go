// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

func matrixBlockSum(mat [][]int, k int) [][]int {
	m, n := len(mat), len(mat[0])
	prefix := make([][]int, m+1)
	for i := range prefix {
		prefix[i] = make([]int, n+1)
	}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			prefix[r+1][c+1] = mat[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]
		}
	}
	answer := make([][]int, m)
	for r := 0; r < m; r++ {
		answer[r] = make([]int, n)
		for c := 0; c < n; c++ {
			r1, c1 := r-k, c-k
			if r1 < 0 {
				r1 = 0
			}
			if c1 < 0 {
				c1 = 0
			}
			r2, c2 := r+k+1, c+k+1
			if r2 > m {
				r2 = m
			}
			if c2 > n {
				c2 = n
			}
			answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
		}
	}
	return answer
}
