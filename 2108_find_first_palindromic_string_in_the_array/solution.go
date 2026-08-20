// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

func firstPalindrome(words []string) string {
	for _, w := range words {
		ok := true
		for l, r := 0, len(w)-1; l < r; l, r = l+1, r-1 {
			if w[l] != w[r] {
				ok = false
				break
			}
		}
		if ok {
			return w
		}
	}
	return ""
}
