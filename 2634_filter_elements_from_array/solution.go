// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/


func filter(arr []int, fn func(int, int) bool) []int {
	out := []int{}
	for i, x := range arr {
		if fn(x, i) {
			out = append(out, x)
		}
	}
	return out
}
