// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

import "sort"

func maxHeight(cuboids [][]int) int {
	a := make([][]int, len(cuboids))
	for i, c := range cuboids {
		x := append([]int{}, c...)
		sort.Ints(x)
		a[i] = x
	}
	sort.Slice(a, func(i, j int) bool {
		for d := 0; d < 3; d++ {
			if a[i][d] != a[j][d] {
				return a[i][d] < a[j][d]
			}
		}
		return false
	})
	n := len(a)
	dp := make([]int, n)
	best := 0
	for i := 0; i < n; i++ {
		dp[i] = a[i][2]
		for j := 0; j < i; j++ {
			ok := true
			for d := 0; d < 3; d++ {
				if a[j][d] > a[i][d] {
					ok = false
					break
				}
			}
			if ok && dp[j]+a[i][2] > dp[i] {
				dp[i] = dp[j] + a[i][2]
			}
		}
		if dp[i] > best {
			best = dp[i]
		}
	}
	return best
}
