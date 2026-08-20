// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

func beautifulSubstrings(s string, k int) int {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	ans := 0
	n := len(s)
	for i := 0; i < n; i++ {
		v, c := 0, 0
		for j := i; j < n; j++ {
			if isVowel(s[j]) {
				v++
			} else {
				c++
			}
			if v == c && (v*c)%k == 0 {
				ans++
			}
		}
	}
	return ans
}
