// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/


func findTheString(lcp [][]int) string {
	n := len(lcp)
	s := make([]byte, n)
	c := byte('a')
	for i := 0; i < n; i++ {
		if s[i] != 0 {
			continue
		}
		if c > 'z' {
			return ""
		}
		s[i] = c
		for j := i + 1; j < n; j++ {
			if lcp[i][j] > 0 {
				s[j] = c
			}
		}
		c++
	}
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			v := 0
			if s[i] == s[j] {
				v = 1
				if i+1 < n && j+1 < n {
					v += lcp[i+1][j+1]
				}
			}
			if lcp[i][j] != v {
				return ""
			}
		}
	}
	return string(s)
}
