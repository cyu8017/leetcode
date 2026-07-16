// LeetCode 0418 - Sentence Screen Fitting
// https://leetcode.com/problems/sentence-screen-fitting/

func wordsTyping(sentence []string, rows int, cols int) int {
	count := 0
	index := 0
	total := len(sentence)

	for row := 0; row < rows; row++ {
		col := 0
		for {
			word := sentence[index]
			needed := len(word)
			if col > 0 {
				needed++
			}
			if col+needed > cols {
				break
			}
			if col > 0 {
				col++
			}
			col += len(word)
			index = (index + 1) % total
			if index == 0 {
				count++
			}
		}
	}

	return count
}
