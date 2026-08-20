// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

func maximumLength(s string) int {
	n := len(s)
	ans := -1
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if s[j] != s[i] {
				break
			}
			sub := s[i : j+1]
			cnt := 0
			for k := 0; k+len(sub) <= n; k++ {
				if s[k:k+len(sub)] == sub {
					cnt++
				}
			}
			if cnt >= 3 && len(sub) > ans {
				ans = len(sub)
			}
		}
	}
	return ans
}
