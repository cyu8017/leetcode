// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

func findLongestWord(s string, dictionary []string) string {
	isSubsequence := func(word string) bool {
		index := 0
		for _, ch := range s {
			if index < len(word) && word[index] == byte(ch) {
				index++
			}
		}
		return index == len(word)
	}

	best := ""
	for _, word := range dictionary {
		if !isSubsequence(word) {
			continue
		}
		if len(word) > len(best) || (len(word) == len(best) && word < best) {
			best = word
		}
	}
	return best
}
