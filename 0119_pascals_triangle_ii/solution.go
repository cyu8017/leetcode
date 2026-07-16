// LeetCode 0119 - Pascal's Triangle II
func getRow(rowIndex int) []int {
	row := make([]int, rowIndex+1)
	for i := range row { row[i] = 1; for j := i-1; j > 0; j-- { row[j] += row[j-1] } }
	return row
}