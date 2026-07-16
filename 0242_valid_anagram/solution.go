// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	counts := [26]int{}
	for index := 0; index < len(s); index++ {
		counts[s[index]-'a']++
		counts[t[index]-'a']--
	}
	for _, count := range counts {
		if count != 0 {
			return false
		}
	}
	return true
}
