// LeetCode 1572 - Matrix Diagonal Sum
// https://leetcode.com/problems/matrix-diagonal-sum/

func diagonalSum(mat [][]int) int {
	n := len(mat)
	ans := 0
	for i := 0; i < n; i++ {
		ans += mat[i][i] + mat[i][n-1-i]
	}
	if n%2 == 1 {
		ans -= mat[n/2][n/2]
	}
	return ans
}
