// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

func getWordsInLongestSubsequence(words []string, groups []int) []string {
	n := len(words)
	dp := make([]int, n)
	prev := make([]int, n)
	for i := range dp {
		dp[i] = 1
		prev[i] = -1
	}
	hamming := func(a, b string) int {
		if len(a) != len(b) {
			return 100
		}
		d := 0
		for i := 0; i < len(a); i++ {
			if a[i] != b[i] {
				d++
			}
		}
		return d
	}
	best, bestI := 1, 0
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if groups[i] != groups[j] && hamming(words[i], words[j]) == 1 && dp[j]+1 > dp[i] {
				dp[i] = dp[j] + 1
				prev[i] = j
			}
		}
		if dp[i] > best {
			best, bestI = dp[i], i
		}
	}
	path := []string{}
	for bestI != -1 {
		path = append(path, words[bestI])
		bestI = prev[bestI]
	}
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	return path
}
