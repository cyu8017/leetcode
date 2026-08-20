// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

import "strconv"

func minimumBeautifulSubstrings(s string) int {
	n := len(s)
	pow5 := map[string]bool{}
	for x := 1; ; x *= 5 {
		b := strconv.FormatInt(int64(x), 2)
		if len(b) > n {
			break
		}
		pow5[b] = true
	}
	const inf = 1 << 30
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	for i := 0; i < n; i++ {
		if dp[i] == inf || s[i] == '0' {
			continue
		}
		for j := i + 1; j <= n; j++ {
			if pow5[s[i:j]] {
				if dp[i]+1 < dp[j] {
					dp[j] = dp[i] + 1
				}
			}
		}
	}
	if dp[n] == inf {
		return -1
	}
	return dp[n]
}
