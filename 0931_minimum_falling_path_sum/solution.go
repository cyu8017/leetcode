// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

func minFallingPathSum(matrix [][]int) int {
	dp := append([]int{}, matrix[0]...)
	for r := 1; r < len(matrix); r++ {
		ndp := make([]int, len(dp))
		for c := 0; c < len(dp); c++ {
			best := dp[c]
			if c > 0 && dp[c-1] < best {
				best = dp[c-1]
			}
			if c+1 < len(dp) && dp[c+1] < best {
				best = dp[c+1]
			}
			ndp[c] = matrix[r][c] + best
		}
		dp = ndp
	}
	ans := dp[0]
	for _, v := range dp[1:] {
		if v < ans {
			ans = v
		}
	}
	return ans
}
