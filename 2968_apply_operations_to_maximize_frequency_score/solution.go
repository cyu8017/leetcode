// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

import "sort"

func maxFrequencyScore(nums []int, k int64) int {
	sort.Ints(nums)
	n := len(nums)
	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(nums[i])
	}
	cost := func(l, r int) int64 {
		mid := (l + r) / 2
		left := int64(nums[mid])*int64(mid-l) - (pref[mid] - pref[l])
		right := (pref[r+1] - pref[mid+1]) - int64(nums[mid])*int64(r-mid)
		return left + right
	}
	ans := 1
	left := 0
	for right := 0; right < n; right++ {
		for cost(left, right) > k {
			left++
		}
		if right-left+1 > ans {
			ans = right - left + 1
		}
	}
	return ans
}
