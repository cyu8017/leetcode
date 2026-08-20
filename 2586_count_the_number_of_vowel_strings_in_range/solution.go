// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/


func vowelStrings(words []string, left int, right int) int {
	isV := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	ans := 0
	for i := left; i <= right; i++ {
		w := words[i]
		if isV(w[0]) && isV(w[len(w)-1]) {
			ans++
		}
	}
	return ans
}
