// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

func countSubstrings(s string) int {
	expand := func(left, right int) int {
		count := 0
		for left >= 0 && right < len(s) && s[left] == s[right] {
			count++
			left--
			right++
		}
		return count
	}
	total := 0
	for i := 0; i < len(s); i++ {
		total += expand(i, i)
		total += expand(i, i+1)
	}
	return total
}
