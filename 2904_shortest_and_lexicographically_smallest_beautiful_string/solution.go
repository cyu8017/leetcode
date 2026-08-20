// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

func shortestBeautifulSubstring(s string, k int) string {
	ans := ""
	n := len(s)
	for i := 0; i < n; i++ {
		ones := 0
		for j := i; j < n; j++ {
			if s[j] == '1' {
				ones++
			}
			if ones == k {
				cand := s[i : j+1]
				if ans == "" || len(cand) < len(ans) || (len(cand) == len(ans) && cand < ans) {
					ans = cand
				}
				break
			}
			if ones > k {
				break
			}
		}
	}
	return ans
}
