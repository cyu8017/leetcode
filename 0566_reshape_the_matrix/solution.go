// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

func matrixReshape(mat [][]int, r int, c int) [][]int {
	rows, cols := len(mat), len(mat[0])
	if rows*cols != r*c {
		return mat
	}
	flat := make([]int, 0, rows*cols)
	for _, row := range mat {
		flat = append(flat, row...)
	}
	result := make([][]int, r)
	for i := 0; i < r; i++ {
		result[i] = flat[i*c : (i+1)*c]
	}
	return result
}
