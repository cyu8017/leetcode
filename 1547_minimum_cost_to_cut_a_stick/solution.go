// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

import "sort"

func minCost(n int, cuts []int) int {
	points := append([]int{0}, append(append([]int{}, cuts...), n)...)
	sort.Ints(points)
	size := len(points)
	dp := make([][]int, size)
	for i := range dp {
		dp[i] = make([]int, size)
	}
	for width := 2; width < size; width++ {
		for left := 0; left+width < size; left++ {
			right := left + width
			best := int(1e18)
			for mid := left + 1; mid < right; mid++ {
				cand := dp[left][mid] + dp[mid][right]
				if cand < best {
					best = cand
				}
			}
			if right > left+1 {
				best += points[right] - points[left]
			} else {
				best = 0
			}
			dp[left][right] = best
		}
	}
	return dp[0][size-1]
}
