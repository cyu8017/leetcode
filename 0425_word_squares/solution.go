// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

import "sort"

func wordSquares(words []string) [][]string {
	sort.Strings(words)
	length := len(words[0])
	prefixMap := map[string][]string{"": append([]string(nil), words...)}

	for _, word := range words {
		for index := 0; index < len(word); index++ {
			prefix := word[:index+1]
			prefixMap[prefix] = append(prefixMap[prefix], word)
		}
	}

	squares := make([][]string, 0)
	current := make([]string, 0, length)

	var dfs func(row int)
	dfs = func(row int) {
		if row == length {
			copySquare := append([]string(nil), current...)
			squares = append(squares, copySquare)
			return
		}

		prefix := make([]byte, row)
		for index, word := range current {
			prefix[index] = word[row]
		}

		for _, candidate := range prefixMap[string(prefix)] {
			current = append(current, candidate)
			dfs(row + 1)
			current = current[:len(current)-1]
		}
	}

	dfs(0)
	return squares
}
