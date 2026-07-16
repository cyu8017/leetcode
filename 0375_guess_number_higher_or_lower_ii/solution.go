// LeetCode 0375 - Guess Number Higher or Lower II
// https://leetcode.com/problems/guess-number-higher-or-lower-ii/

import "math"

func getMoneyAmount(n int) int {
	dp := make([][]int, n+2)
	for index := range dp {
		dp[index] = make([]int, n+2)
	}

	for length := 2; length <= n; length++ {
		for left := 1; left <= n-length+1; left++ {
			right := left + length - 1
			dp[left][right] = math.MaxInt32
			for guess := left; guess < right; guess++ {
				cost := guess
				if dp[left][guess-1] > dp[guess+1][right] {
					cost += dp[left][guess-1]
				} else {
					cost += dp[guess+1][right]
				}
				if cost < dp[left][right] {
					dp[left][right] = cost
				}
			}
		}
	}

	return dp[1][n]
}
