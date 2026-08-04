// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

func findPeakGrid(mat [][]int) []int {
	rows, cols := len(mat), len(mat[0])
	lo, hi := 0, cols-1
	for lo <= hi {
		mid := (lo + hi) / 2
		maxRow := 0
		for r := 1; r < rows; r++ {
			if mat[r][mid] > mat[maxRow][mid] {
				maxRow = r
			}
		}
		left := -1
		if mid > 0 {
			left = mat[maxRow][mid-1]
		}
		right := -1
		if mid+1 < cols {
			right = mat[maxRow][mid+1]
		}
		if mat[maxRow][mid] >= left && mat[maxRow][mid] >= right {
			return []int{maxRow, mid}
		}
		if left > mat[maxRow][mid] {
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return []int{0, 0}
}
