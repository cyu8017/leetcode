// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

func validWordSquare(words []string) bool {
	for row, word := range words {
		for col := 0; col < len(word); col++ {
			if col >= len(words) || row >= len(words[col]) || words[col][row] != word[col] {
				return false
			}
		}
	}
	return true
}
