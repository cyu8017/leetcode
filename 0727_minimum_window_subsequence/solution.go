// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

func minWindow(s1 string, s2 string) string {
	m, n := len(s1), len(s2)
	best := ""
	i := 0
	for i < m {
		j, k := 0, i
		for k < m && j < n {
			if s1[k] == s2[j] {
				j++
			}
			k++
		}
		if j < n {
			break
		}
		end := k - 1
		j = n - 1
		k = end
		for j >= 0 {
			if s1[k] == s2[j] {
				j--
			}
			k--
		}
		start := k + 1
		if best == "" || end-start+1 < len(best) {
			best = s1[start : end+1]
		}
		i = start + 1
	}
	return best
}
