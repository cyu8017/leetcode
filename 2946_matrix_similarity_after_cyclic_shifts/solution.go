// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

func areSimilar(mat [][]int, k int) bool {
	m, n := len(mat), len(mat[0])
	k %= n
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			nj := j
			if i%2 == 0 {
				nj = (j - k + 10000*n) % n
			} else {
				nj = (j + k) % n
			}
			if mat[i][j] != mat[i][nj] {
				// compare original to shifted result: row should equal itself after shift
			}
		}
	}
	for i := 0; i < m; i++ {
		shift := k
		if i%2 == 0 {
			shift = n - (k % n)
			if shift == n {
				shift = 0
			}
		} else {
			shift = k % n
		}
		for j := 0; j < n; j++ {
			if mat[i][j] != mat[i][(j+shift)%n] {
				return false
			}
		}
	}
	return true
}
