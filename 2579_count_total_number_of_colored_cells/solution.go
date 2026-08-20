// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/


func coloredCells(n int) int64 {
	return 1 + 2*int64(n)*int64(n-1)
}
