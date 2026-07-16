// LeetCode 0316 - Remove Duplicate Letters
// https://leetcode.com/problems/remove-duplicate-letters/

func removeDuplicateLetters(s string) string {
	lastIndex := make(map[byte]int)
	for index := 0; index < len(s); index++ {
		lastIndex[s[index]] = index
	}

	stack := make([]byte, 0, len(s))
	seen := make(map[byte]bool)
	for index := 0; index < len(s); index++ {
		character := s[index]
		if seen[character] {
			continue
		}
		for len(stack) > 0 && stack[len(stack)-1] > character && lastIndex[stack[len(stack)-1]] > index {
			seen[stack[len(stack)-1]] = false
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, character)
		seen[character] = true
	}

	return string(stack)
}
