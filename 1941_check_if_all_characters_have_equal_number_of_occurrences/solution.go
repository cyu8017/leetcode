// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

func areOccurrencesEqual(s string) bool {
	freq := make([]int, 26)
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	target := 0
	for _, f := range freq {
		if f == 0 {
			continue
		}
		if target == 0 {
			target = f
		} else if f != target {
			return false
		}
	}
	return true
}
