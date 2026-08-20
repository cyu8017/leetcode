// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

import "sort"

func sumSubseqWidths(nums []int) int {
	const MOD = 1_000_000_007
	sort.Ints(nums)
	n := len(nums)
	pow2 := make([]int, n)
	pow2[0] = 1
	for i := 1; i < n; i++ {
		pow2[i] = (pow2[i-1] * 2) % MOD
	}
	ans := 0
	for i, x := range nums {
		ans = (ans + x*(pow2[i]-pow2[n-1-i])) % MOD
	}
	return (ans + MOD) % MOD
}
