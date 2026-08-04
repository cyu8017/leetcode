// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

import "sort"

func maxJumps(arr []int, d int) int {
	n := len(arr)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = 1
	}
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool { return arr[order[i]] < arr[order[j]] })
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	for _, i := range order {
		for _, step := range []int{-1, 1} {
			j := i + step
			for j >= 0 && j < n && abs(j-i) <= d && arr[j] < arr[i] {
				if 1+dp[j] > dp[i] {
					dp[i] = 1 + dp[j]
				}
				j += step
			}
		}
	}
	best := 0
	for _, v := range dp {
		if v > best {
			best = v
		}
	}
	return best
}
