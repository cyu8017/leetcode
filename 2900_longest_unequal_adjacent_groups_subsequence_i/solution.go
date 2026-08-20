// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

func getLongestSubsequence(words []string, groups []int) []string {
	ans := []string{words[0]}
	last := groups[0]
	for i := 1; i < len(words); i++ {
		if groups[i] != last {
			ans = append(ans, words[i])
			last = groups[i]
		}
	}
	return ans
}
