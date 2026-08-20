// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/


func vowelStrings(words []string, queries [][]int) []int {
	isV := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	pref := make([]int, len(words)+1)
	for i, w := range words {
		pref[i+1] = pref[i]
		if len(w) > 0 && isV(w[0]) && isV(w[len(w)-1]) {
			pref[i+1]++
		}
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		ans[i] = pref[q[1]+1] - pref[q[0]]
	}
	return ans
}
