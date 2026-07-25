// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

import "sort"

func closeStrings(word1, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}
	var c1, c2 [26]int
	for i := 0; i < len(word1); i++ {
		c1[word1[i]-'a']++
		c2[word2[i]-'a']++
	}
	v1, v2 := []int{}, []int{}
	for i := 0; i < 26; i++ {
		if (c1[i] == 0) != (c2[i] == 0) {
			return false
		}
		if c1[i] > 0 {
			v1 = append(v1, c1[i])
			v2 = append(v2, c2[i])
		}
	}
	sort.Ints(v1)
	sort.Ints(v2)
	for i := range v1 {
		if v1[i] != v2[i] {
			return false
		}
	}
	return true
}
