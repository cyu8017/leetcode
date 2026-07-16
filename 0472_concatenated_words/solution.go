// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

import "sort"

func canForm(word string, dictionary map[string]struct{}) bool {
	if word == "" {
		return true
	}
	length := len(word)
	dp := make([]bool, length+1)
	dp[0] = true
	for end := 1; end <= length; end++ {
		for start := 0; start < end; start++ {
			if dp[start] {
				if _, ok := dictionary[word[start:end]]; ok {
					dp[end] = true
					break
				}
			}
		}
	}
	return dp[length]
}

func findAllConcatenatedWordsInADict(words []string) []string {
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})

	wordSet := make(map[string]struct{}, len(words))
	for _, word := range words {
		wordSet[word] = struct{}{}
	}

	result := make([]string, 0)
	for _, word := range words {
		delete(wordSet, word)
		if canForm(word, wordSet) {
			result = append(result, word)
		}
		wordSet[word] = struct{}{}
	}
	return result
}
