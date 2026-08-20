// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/


func longestSemiRepetitiveSubstring(s string) int {
	ans, left, lastPair := 0, 0, -1
	for right := 0; right < len(s); right++ {
		if right > 0 && s[right] == s[right-1] {
			if lastPair >= left {
				left = lastPair + 1
			}
			lastPair = right - 1
		}
		if right-left+1 > ans {
			ans = right - left + 1
		}
	}
	return ans
}
