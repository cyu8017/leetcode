// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

func longestContinuousSubstring(s string) int {
	ans, cur := 1, 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1]+1 {
			cur++
			if cur > ans {
				ans = cur
			}
		} else {
			cur = 1
		}
	}
	return ans
}
