// LeetCode 0378 - Kth Smallest Element in a Sorted Matrix
// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

func kthSmallest(matrix [][]int, k int) int {
	rows := len(matrix)
	left := matrix[0][0]
	right := matrix[rows-1][rows-1]

	for left < right {
		mid := left + (right-left)/2
		count := 0
		column := rows - 1

		for row := 0; row < rows; row++ {
			for column >= 0 && matrix[row][column] > mid {
				column--
			}
			count += column + 1
		}

		if count < k {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}
