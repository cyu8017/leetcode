// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

import "math/bits"

func maxScore(nums []int) int {
	n := len(nums)
	memo := make([]int, 1<<n)
	for i := range memo {
		memo[i] = -1
	}
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	var dp func(mask int) int
	dp = func(mask int) int {
		if mask == (1<<n)-1 {
			return 0
		}
		if memo[mask] != -1 {
			return memo[mask]
		}
		step := bits.OnesCount(uint(mask))/2 + 1
		best := 0
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 {
				continue
			}
			for j := i + 1; j < n; j++ {
				if mask>>j&1 == 1 {
					continue
				}
				score := step*gcd(nums[i], nums[j]) + dp(mask|1<<i|1<<j)
				if score > best {
					best = score
				}
			}
		}
		memo[mask] = best
		return best
	}
	return dp(0)
}
