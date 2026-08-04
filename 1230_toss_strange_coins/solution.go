// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

func probabilityOfHeads(prob []float64, target int) float64 {
	dp := make([]float64, target+1)
	dp[0] = 1
	for _, p := range prob {
		for heads := target; heads >= 0; heads-- {
			v := dp[heads] * (1 - p)
			if heads > 0 {
				v += dp[heads-1] * p
			}
			dp[heads] = v
		}
	}
	return dp[target]
}
