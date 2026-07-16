// LeetCode 0363 - Max Sum of Rectangle No Larger Than K
// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

import "sort"

func maxSumSubmatrix(matrix [][]int, k int) int {
	rows := len(matrix)
	if rows == 0 {
		return 0
	}
	cols := len(matrix[0])
	result := -1 << 30

	for top := 0; top < rows; top++ {
		colSums := make([]int, cols)
		for bottom := top; bottom < rows; bottom++ {
			prefixSums := []int{0}
			running := 0

			for col := 0; col < cols; col++ {
				colSums[col] += matrix[bottom][col]
				running += colSums[col]

				index := sort.SearchInts(prefixSums, running-k)
				if index < len(prefixSums) {
					if candidate := running - prefixSums[index]; candidate > result {
						result = candidate
					}
				}

				insertIndex := sort.SearchInts(prefixSums, running)
				prefixSums = append(prefixSums, 0)
				copy(prefixSums[insertIndex+1:], prefixSums[insertIndex:])
				prefixSums[insertIndex] = running
			}
		}
	}

	return result
}
