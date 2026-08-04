// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

import "strings"

func reorderSpaces(text string) string {
	words := strings.Fields(text)
	spaces := strings.Count(text, " ")
	if len(words) == 1 {
		return words[0] + strings.Repeat(" ", spaces)
	}
	between := spaces / (len(words) - 1)
	trailing := spaces % (len(words) - 1)
	return strings.Join(words, strings.Repeat(" ", between)) + strings.Repeat(" ", trailing)
}
