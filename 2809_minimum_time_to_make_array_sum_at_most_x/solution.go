// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

import "sort"

func minimumTime(nums1 []int, nums2 []int, x int) int {
	n := len(nums1)
	type pair struct{ a, b int }
	arr := make([]pair, n)
	sum1, sum2 := 0, 0
	for i := 0; i < n; i++ {
		arr[i] = pair{nums1[i], nums2[i]}
		sum1 += nums1[i]
		sum2 += nums2[i]
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].b < arr[j].b })
	dp := make([]int, n+1)
	for i := 0; i < n; i++ {
		for j := i + 1; j >= 1; j-- {
			cand := dp[j-1] + arr[i].a + j*arr[i].b
			if cand > dp[j] {
				dp[j] = cand
			}
		}
	}
	for t := 0; t <= n; t++ {
		if sum1+sum2*t-dp[t] <= x {
			return t
		}
	}
	return -1
}
