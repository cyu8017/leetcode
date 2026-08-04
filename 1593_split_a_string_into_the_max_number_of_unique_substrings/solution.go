// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

func maxUniqueSplit(s string) int {
	used := map[string]bool{}
	answer := 0
	var dfs func(int)
	dfs = func(i int) {
		if len(used)+len(s)-i <= answer {
			return
		}
		if i == len(s) {
			if len(used) > answer {
				answer = len(used)
			}
			return
		}
		for j := i + 1; j <= len(s); j++ {
			part := s[i:j]
			if !used[part] {
				used[part] = true
				dfs(j)
				delete(used, part)
			}
		}
	}
	dfs(0)
	return answer
}
