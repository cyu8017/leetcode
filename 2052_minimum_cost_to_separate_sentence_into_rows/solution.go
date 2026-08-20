// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

import "strings"

func minimumCost(sentence string, k int) int {
	words := strings.Fields(sentence)
	n := len(words)
	inf := int(1e18)
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = inf
	}
	dp[n] = 0
	for i := n - 1; i >= 0; i-- {
		length := -1
		for j := i; j < n; j++ {
			length += 1 + len(words[j])
			if length > k {
				break
			}
			cost := 0
			if j < n-1 {
				extra := k - length
				cost = extra * extra
			}
			if cost+dp[j+1] < dp[i] {
				dp[i] = cost + dp[j+1]
			}
		}
	}
	return dp[0]
}
