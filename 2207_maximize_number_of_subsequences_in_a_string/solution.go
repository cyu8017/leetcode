// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

func maximumSubsequenceCount(text string, pattern string) int64 {
	a, b := pattern[0], pattern[1]
	count := func(s string) int64 {
		var ca, ans int64
		for i := 0; i < len(s); i++ {
			if s[i] == b {
				ans += ca
			}
			if s[i] == a {
				ca++
			}
		}
		return ans
	}
	c1 := count(string(a) + text)
	c2 := count(text + string(b))
	if c1 > c2 {
		return c1
	}
	return c2
}
