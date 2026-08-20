// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

func maximizeTheProfit(n int, offers [][]int) int {
	byEnd := make([][][]int, n)
	for _, o := range offers {
		byEnd[o[1]] = append(byEnd[o[1]], o)
	}
	dp := make([]int, n+1)
	for end := 0; end < n; end++ {
		dp[end+1] = dp[end]
		for _, o := range byEnd[end] {
			cand := dp[o[0]] + o[2]
			if cand > dp[end+1] {
				dp[end+1] = cand
			}
		}
	}
	return dp[n]
}
