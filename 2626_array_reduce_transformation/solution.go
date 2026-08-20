// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/


func reduce(nums []int, fn func(int, int) int, init int) int {
	acc := init
	for _, x := range nums {
		acc = fn(acc, x)
	}
	return acc
}
