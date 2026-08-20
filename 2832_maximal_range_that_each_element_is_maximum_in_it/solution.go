// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

func maximumLength(nums []int) []int {
	n := len(nums)
	left := make([]int, n)
	right := make([]int, n)
	st := []int{}
	for i := 0; i < n; i++ {
		for len(st) > 0 && nums[st[len(st)-1]] < nums[i] {
			st = st[:len(st)-1]
		}
		if len(st) == 0 {
			left[i] = -1
		} else {
			left[i] = st[len(st)-1]
		}
		st = append(st, i)
	}
	st = st[:0]
	for i := n - 1; i >= 0; i-- {
		for len(st) > 0 && nums[st[len(st)-1]] <= nums[i] {
			st = st[:len(st)-1]
		}
		if len(st) == 0 {
			right[i] = n
		} else {
			right[i] = st[len(st)-1]
		}
		st = append(st, i)
	}
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = right[i] - left[i] - 1
	}
	return ans
}
