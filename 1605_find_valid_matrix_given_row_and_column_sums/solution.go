// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

func restoreMatrix(rowSum []int, colSum []int) [][]int {
	ans := make([][]int, len(rowSum))
	for i := range ans {
		ans[i] = make([]int, len(colSum))
	}
	i, j := 0, 0
	for i < len(rowSum) && j < len(colSum) {
		x := rowSum[i]
		if colSum[j] < x {
			x = colSum[j]
		}
		ans[i][j] = x
		rowSum[i] -= x
		colSum[j] -= x
		if rowSum[i] == 0 {
			i++
		}
		if colSum[j] == 0 {
			j++
		}
	}
	return ans
}
