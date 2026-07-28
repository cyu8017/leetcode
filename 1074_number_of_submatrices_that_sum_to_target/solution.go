// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

func numSubmatrixSumTarget(matrix [][]int, target int) int {
	rows, cols := len(matrix), len(matrix[0])
	ans := 0
	for left := 0; left < cols; left++ {
		rowSum := make([]int, rows)
		for right := left; right < cols; right++ {
			for r := 0; r < rows; r++ {
				rowSum[r] += matrix[r][right]
			}
			prefix := 0
			seen := map[int]int{0: 1}
			for _, val := range rowSum {
				prefix += val
				ans += seen[prefix-target]
				seen[prefix]++
			}
		}
	}
	return ans
}
