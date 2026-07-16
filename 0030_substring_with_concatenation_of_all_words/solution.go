// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

func findSubstring(s string, words []string) []int {
	if len(words) == 0 || len(s) == 0 {
		return []int{}
	}
	wordLen := len(words[0])
	wordCount := len(words)
	need := make(map[string]int)
	for _, word := range words {
		need[word]++
	}
	result := make([]int, 0)

	for start := 0; start < wordLen; start++ {
		left := start
		counts := make(map[string]int)
		used := 0
		for right := start; right <= len(s)-wordLen; right += wordLen {
			word := s[right : right+wordLen]
			if need[word] == 0 {
				counts = make(map[string]int)
				used = 0
				left = right + wordLen
				continue
			}
			counts[word]++
			used++
			for counts[word] > need[word] {
				leftWord := s[left : left+wordLen]
				counts[leftWord]--
				used--
				left += wordLen
			}
			if used == wordCount {
				result = append(result, left)
			}
		}
	}
	return result
}
