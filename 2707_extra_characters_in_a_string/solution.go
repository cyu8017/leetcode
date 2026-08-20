// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/


func minExtraChar(s string, dictionary []string) int {
	dict := map[string]bool{}
	for _, w := range dictionary {
		dict[w] = true
	}
	n := len(s)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = dp[i-1] + 1
		for j := 0; j < i; j++ {
			if dict[s[j:i]] && dp[j] < dp[i] {
				dp[i] = dp[j]
			}
		}
	}
	return dp[n]
}
