// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

func lengthOfLastWord(s string) int {
	length := 0
	i := len(s) - 1

	for i >= 0 && s[i] == ' ' {
		i--
	}

	for i >= 0 && s[i] != ' ' {
		length++
		i--
	}

	return length
}
