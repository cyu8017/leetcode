// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

func makeEqual(words []string) bool {
	counts := make(map[rune]int)
	for _, word := range words {
		for _, ch := range word {
			counts[ch]++
		}
	}
	n := len(words)
	for _, total := range counts {
		if total%n != 0 {
			return false
		}
	}
	return true
}
