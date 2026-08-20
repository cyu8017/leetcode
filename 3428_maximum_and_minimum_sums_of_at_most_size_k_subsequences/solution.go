// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

import "sort"

func minMaxSums(nums []int, k int) int {
	const mod = 1000000007
	sort.Ints(nums)
	n := len(nums)
	// C[i][j] for j<=k-1
	C := make([][]int, n+1)
	for i := range C {
		C[i] = make([]int, k)
		C[i][0] = 1
		for j := 1; j < k && j <= i; j++ {
			C[i][j] = (C[i-1][j] + C[i-1][j-1]) % mod
		}
	}
	ans := 0
	for i := 0; i < n; i++ {
		// as max: choose at most k-1 from left
		waysMax := 0
		for j := 0; j < k && j <= i; j++ {
			waysMax = (waysMax + C[i][j]) % mod
		}
		// as min: choose at most k-1 from right
		waysMin := 0
		right := n - i - 1
		for j := 0; j < k && j <= right; j++ {
			waysMin = (waysMin + C[right][j]) % mod
		}
		ans = (ans + nums[i]*waysMax%mod + nums[i]*waysMin%mod) % mod
	}
	return ans
}
