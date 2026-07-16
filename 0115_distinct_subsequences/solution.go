// LeetCode 0115 - Distinct Subsequences
func numDistinct(s string, t string) int {
	dp := make([]uint64, len(t)+1); dp[0] = 1
	for i := range s { for j := len(t); j > 0; j-- {
		if s[i] == t[j-1] { dp[j] += dp[j-1] }
	} }
	return int(dp[len(t)])
}