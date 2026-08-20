// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

func uniqueMorseRepresentations(words []string) int {
	codes := []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}
	seen := map[string]bool{}
	for _, word := range words {
		var b []byte
		for i := 0; i < len(word); i++ {
			b = append(b, codes[word[i]-'a']...)
		}
		seen[string(b)] = true
	}
	return len(seen)
}
