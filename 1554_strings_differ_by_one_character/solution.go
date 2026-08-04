// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

func differByOne(dict []string) bool {
	seen := map[string]bool{}
	for _, word := range dict {
		b := []byte(word)
		for i := range b {
			orig := b[i]
			b[i] = '*'
			pattern := string(b)
			if seen[pattern] {
				return true
			}
			seen[pattern] = true
			b[i] = orig
		}
	}
	return false
}
