// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

func removeInvalidParentheses(s string) []string {
	isValid := func(text string) bool {
		balance := 0
		for _, character := range text {
			if character == '(' {
				balance++
			} else if character == ')' {
				if balance == 0 {
					return false
				}
				balance--
			}
		}
		return balance == 0
	}

	result := make(map[string]struct{})
	queue := []string{s}
	visited := map[string]struct{}{s: {}}
	found := false

	for len(queue) > 0 {
		levelSize := len(queue)
		for level := 0; level < levelSize; level++ {
			current := queue[0]
			queue = queue[1:]
			if isValid(current) {
				result[current] = struct{}{}
				found = true
			}
			if found {
				continue
			}
			for index := 0; index < len(current); index++ {
				if current[index] != '(' && current[index] != ')' {
					continue
				}
				next := current[:index] + current[index+1:]
				if _, seen := visited[next]; !seen {
					visited[next] = struct{}{}
					queue = append(queue, next)
				}
			}
		}
	}

	answers := make([]string, 0, len(result))
	for answer := range result {
		answers = append(answers, answer)
	}
	return answers
}
