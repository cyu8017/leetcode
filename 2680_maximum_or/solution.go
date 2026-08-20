// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/


func maximumOr(nums []int, k int) int64 {
	n := len(nums)
	suf := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		suf[i] = suf[i+1] | nums[i]
	}
	var pref, ans int64
	for i := 0; i < n; i++ {
		cand := pref | (int64(nums[i]) << k) | int64(suf[i+1])
		if cand > ans {
			ans = cand
		}
		pref |= int64(nums[i])
	}
	return ans
}
