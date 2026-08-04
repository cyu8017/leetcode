// LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

func maxVowels(s string, k int) int {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	cur := 0
	for i := 0; i < k; i++ {
		if isVowel(s[i]) {
			cur++
		}
	}
	ans := cur
	for i := k; i < len(s); i++ {
		if isVowel(s[i]) {
			cur++
		}
		if isVowel(s[i-k]) {
			cur--
		}
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
