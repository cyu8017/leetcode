// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

func maxPoints(points [][]int) int64 {
	m, n := len(points), len(points[0])
	dp := make([]int64, n)
	for c := 0; c < n; c++ {
		dp[c] = int64(points[0][c])
	}
	for r := 1; r < m; r++ {
		left := make([]int64, n)
		right := make([]int64, n)
		left[0] = dp[0]
		for c := 1; c < n; c++ {
			left[c] = left[c-1] - 1
			if dp[c] > left[c] {
				left[c] = dp[c]
			}
		}
		right[n-1] = dp[n-1]
		for c := n - 2; c >= 0; c-- {
			right[c] = right[c+1] - 1
			if dp[c] > right[c] {
				right[c] = dp[c]
			}
		}
		ndp := make([]int64, n)
		for c := 0; c < n; c++ {
			best := left[c]
			if right[c] > best {
				best = right[c]
			}
			ndp[c] = int64(points[r][c]) + best
		}
		dp = ndp
	}
	best := dp[0]
	for _, v := range dp[1:] {
		if v > best {
			best = v
		}
	}
	return best
}
