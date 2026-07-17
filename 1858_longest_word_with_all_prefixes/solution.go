// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

func longestWord(words []string) string {
	wordSet := make(map[string]struct{}, len(words))
	for _, word := range words {
		wordSet[word] = struct{}{}
	}

	best := ""
	for _, word := range words {
		prefix := word
		valid := true
		for len(prefix) > 0 {
			if _, ok := wordSet[prefix]; !ok {
				valid = false
				break
			}
			prefix = prefix[:len(prefix)-1]
		}
		if valid && (len(word) > len(best) || (len(word) == len(best) && word < best)) {
			best = word
		}
	}

	return best
}
