// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

import "sort"

func numFactoredBinaryTrees(arr []int) int {
	const MOD = 1000000007
	sort.Ints(arr)
	dp := map[int]int{}
	for i, x := range arr {
		ways := 1
		for j := 0; j < i; j++ {
			left := arr[j]
			if x%left == 0 {
				right := x / left
				if _, ok := dp[right]; ok {
					ways = (ways + dp[left]*dp[right]) % MOD
				}
			}
		}
		dp[x] = ways
	}
	ans := 0
	for _, v := range dp {
		ans = (ans + v) % MOD
	}
	return ans
}
