// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

type NumMatrix struct {
	prefix [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	rows := len(matrix)
	cols := 0
	if rows > 0 {
		cols = len(matrix[0])
	}
	prefix := make([][]int, rows+1)
	for row := range prefix {
		prefix[row] = make([]int, cols+1)
	}
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			prefix[row+1][col+1] = matrix[row][col] + prefix[row][col+1] + prefix[row+1][col] - prefix[row][col]
		}
	}
	return NumMatrix{prefix: prefix}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	topLeft := this.prefix[row1][col1]
	topRight := this.prefix[row1][col2+1]
	bottomLeft := this.prefix[row2+1][col1]
	bottomRight := this.prefix[row2+1][col2+1]
	return bottomRight - topRight - bottomLeft + topLeft
}
