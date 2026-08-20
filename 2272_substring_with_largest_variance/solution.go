// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

func largestVariance(s string) int {
	ans := 0
	for a := byte('a'); a <= 'z'; a++ {
		for b := byte('a'); b <= 'z'; b++ {
			if a == b {
				continue
			}
			bal, hasB := 0, false
			for i := 0; i < len(s); i++ {
				if s[i] == a {
					bal++
				} else if s[i] == b {
					bal--
					hasB = true
				}
				if hasB && bal > ans {
					ans = bal
				}
				if bal < 0 {
					bal = 0
					hasB = false
				}
			}
		}
	}
	return ans
}
