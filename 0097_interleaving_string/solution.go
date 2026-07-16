// LeetCode 0097 - Interleaving String
// https://leetcode.com/problems/interleaving-string/

func isInterleave(s1 string, s2 string, s3 string) bool {
	if len(s1)+len(s2) != len(s3) {
		return false
	}

	m := len(s1)
	n := len(s2)
	dp := make([]bool, n+1)
	dp[0] = true

	for j := 1; j <= n; j++ {
		dp[j] = dp[j-1] && s2[j-1] == s3[j-1]
	}

	for i := 1; i <= m; i++ {
		dp[0] = dp[0] && s1[i-1] == s3[i-1]
		for j := 1; j <= n; j++ {
			dp[j] = (dp[j] && s1[i-1] == s3[i+j-1]) || (dp[j-1] && s2[j-1] == s3[i+j-1])
		}
	}

	return dp[n]
}
