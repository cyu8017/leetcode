// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/


func findSmallestInteger(nums []int, value int) int {
	cnt := make([]int, value)
	for _, x := range nums {
		r := x % value
		if r < 0 {
			r += value
		}
		cnt[r]++
	}
	mex := 0
	for cnt[mex%value] > 0 {
		cnt[mex%value]--
		mex++
	}
	return mex
}
