// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

func countPalindromicSubsequence(s string) int {
	first := make(map[byte]int)
	last := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		c := s[i]
		if _, ok := first[c]; !ok {
			first[c] = i
		}
		last[c] = i
	}
	ans := 0
	for c, f := range first {
		l := last[c]
		if l-f > 1 {
			seen := make(map[byte]struct{})
			for i := f + 1; i < l; i++ {
				seen[s[i]] = struct{}{}
			}
			ans += len(seen)
		}
	}
	return ans
}
