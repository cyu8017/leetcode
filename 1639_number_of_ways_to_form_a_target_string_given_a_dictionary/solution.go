// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

func numWays(words []string, target string) int {
	const mod = 1000000007
	m := len(words[0])
	dp := make([]int, len(target)+1)
	dp[0] = 1
	for j := 0; j < m; j++ {
		count := [26]int{}
		for _, word := range words {
			count[word[j]-'a']++
		}
		lim := j + 1
		if lim > len(target) {
			lim = len(target)
		}
		for i := lim; i > 0; i-- {
			dp[i] = (dp[i] + dp[i-1]*count[target[i-1]-'a']) % mod
		}
	}
	return dp[len(target)]
}
