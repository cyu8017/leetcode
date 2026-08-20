// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

func mostPoints(questions [][]int) int64 {
	n := len(questions)
	dp := make([]int64, n+1)
	for i := n - 1; i >= 0; i-- {
		pts, brain := questions[i][0], questions[i][1]
		next := i + brain + 1
		take := int64(pts)
		if next < n {
			take += dp[next]
		}
		dp[i] = dp[i+1]
		if take > dp[i] {
			dp[i] = take
		}
	}
	return dp[0]
}
