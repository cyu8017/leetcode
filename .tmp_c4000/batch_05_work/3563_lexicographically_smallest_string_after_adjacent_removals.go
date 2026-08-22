// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

func lexicographicallySmallestString(s string) string {
	n := len(s)
	dp := make([][]string, n+1)
	for i := range dp {
		dp[i] = make([]string, n+1)
	}
	isConsec := func(a, b byte) bool {
		d := int(a) - int(b)
		if d < 0 {
			d = -d
		}
		return d == 1 || d == 25
	}
	for length := 1; length <= n; length++ {
		for i := 0; i+length <= n; i++ {
			j := i + length
			minStr := string(s[i]) + dp[i+1][j]
			for k := i + 1; k < j; k++ {
				if isConsec(s[i], s[k]) && dp[i+1][k] == "" {
					cand := dp[k+1][j]
					if cand < minStr {
						minStr = cand
					}
				}
			}
			dp[i][j] = minStr
		}
	}
	return dp[0][n]
}
