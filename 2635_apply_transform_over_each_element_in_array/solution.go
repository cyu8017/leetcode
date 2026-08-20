// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/


func map(arr []int, fn func(int, int) int) []int {
	out := make([]int, len(arr))
	for i, x := range arr {
		out[i] = fn(x, i)
	}
	return out
}
