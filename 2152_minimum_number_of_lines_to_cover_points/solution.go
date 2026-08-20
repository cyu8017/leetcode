// LeetCode 2152 - Minimum Number of Lines to Cover Points
// https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

func minimumLines(points [][]int) int {
	n := len(points)
	if n <= 2 {
		return 1
	}
	// same slope check
	colinear := func(a, b, c []int) bool {
		return (b[0]-a[0])*(c[1]-a[1]) == (c[0]-a[0])*(b[1]-a[1])
	}
	inf := n
	dp := make([]int, 1<<n)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	for mask := 0; mask < 1<<n; mask++ {
		if dp[mask] == inf {
			continue
		}
		// pick first uncovered
		i := 0
		for i < n && mask&(1<<i) != 0 {
			i++
		}
		if i == n {
			continue
		}
		// single point line
		nm := mask | (1 << i)
		if dp[mask]+1 < dp[nm] {
			dp[nm] = dp[mask] + 1
		}
		for j := i + 1; j < n; j++ {
			if mask&(1<<j) != 0 {
				continue
			}
			nm := mask | (1 << i) | (1 << j)
			for k := 0; k < n; k++ {
				if nm&(1<<k) == 0 && colinear(points[i], points[j], points[k]) {
					nm |= 1 << k
				}
			}
			if dp[mask]+1 < dp[nm] {
				dp[nm] = dp[mask] + 1
			}
		}
	}
	return dp[(1<<n)-1]
}
