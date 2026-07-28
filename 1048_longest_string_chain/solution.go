// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

import "sort"

func longestStrChain(words []string) int {
	sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
	dp := map[string]int{}
	ans := 1
	for _, w := range words {
		dp[w] = 1
		for i := 0; i < len(w); i++ {
			prev := w[:i] + w[i+1:]
			if v, ok := dp[prev]; ok && v+1 > dp[w] {
				dp[w] = v + 1
			}
		}
		if dp[w] > ans {
			ans = dp[w]
		}
	}
	return ans
}
