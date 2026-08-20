// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

func minValidStrings(words []string, target string) int {
	n := len(target)
	const inf = int(1e9)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = inf
	}
	type trieNode struct {
		next [26]*trieNode
	}
	root := &trieNode{}
	for _, w := range words {
		cur := root
		for _, c := range w {
			ci := c - 'a'
			if cur.next[ci] == nil {
				cur.next[ci] = &trieNode{}
			}
			cur = cur.next[ci]
		}
	}
	for i := 0; i < n; i++ {
		if dp[i] == inf {
			continue
		}
		cur := root
		for j := i; j < n; j++ {
			ci := target[j] - 'a'
			if cur.next[ci] == nil {
				break
			}
			cur = cur.next[ci]
			if dp[i]+1 < dp[j+1] {
				dp[j+1] = dp[i] + 1
			}
		}
	}
	if dp[n] == inf {
		return -1
	}
	return dp[n]
}
