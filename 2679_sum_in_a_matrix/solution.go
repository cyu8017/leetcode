// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/


import "sort"

func matrixSum(nums [][]int) int {
	for i := range nums {
		sort.Ints(nums[i])
	}
	ans := 0
	n := len(nums[0])
	for c := 0; c < n; c++ {
		mx := 0
		for r := range nums {
			if nums[r][c] > mx {
				mx = nums[r][c]
			}
		}
		ans += mx
	}
	return ans
}
