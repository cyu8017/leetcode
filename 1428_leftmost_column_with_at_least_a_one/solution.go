// LeetCode 1428 - Leftmost Column with at Least a One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

type BinaryMatrix interface {
	Get(row, col int) int
	Dimensions() []int
}

func leftMostColumnWithOne(binaryMatrix BinaryMatrix) int {
	dims := binaryMatrix.Dimensions()
	rows, cols := dims[0], dims[1]
	row, col, answer := 0, cols-1, -1
	for row < rows && col >= 0 {
		if binaryMatrix.Get(row, col) == 1 {
			answer = col
			col--
		} else {
			row++
		}
	}
	return answer
}
