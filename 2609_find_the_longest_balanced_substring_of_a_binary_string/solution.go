// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/


func findTheLongestBalancedSubstring(s string) int {
	ans, zeros, ones := 0, 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			if ones > 0 {
				zeros, ones = 0, 0
			}
			zeros++
		} else {
			ones++
			cur := ones
			if zeros < cur {
				cur = zeros
			}
			if 2*cur > ans {
				ans = 2 * cur
			}
		}
	}
	return ans
}
