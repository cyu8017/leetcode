// LeetCode 0388 - Longest Absolute File Path
// https://leetcode.com/problems/longest-absolute-file-path/

import "strings"

func lengthLongestPath(input string) int {
	stack := make([]int, 0)
	maxLength := 0

	for _, line := range strings.Split(input, "\n") {
		depth := 0
		for depth < len(line) && line[depth] == '\t' {
			depth++
		}
		name := line[depth:]

		for len(stack) > depth {
			stack = stack[:len(stack)-1]
		}

		if strings.Contains(name, ".") {
			prefix := 0
			if len(stack) > 0 {
				prefix = stack[len(stack)-1]
			}
			total := prefix + len(name)
			if total > maxLength {
				maxLength = total
			}
		} else {
			prefix := 0
			if len(stack) > 0 {
				prefix = stack[len(stack)-1]
			}
			stack = append(stack, prefix+len(name)+1)
		}
	}

	return maxLength
}
