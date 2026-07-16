// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

func generateParenthesis(n int) []string {
	result := make([]string, 0)
	path := make([]byte, 0, 2*n)

	var backtrack func(open, close int)
	backtrack = func(open, close int) {
		if len(path) == 2*n {
			result = append(result, string(path))
			return
		}
		if open < n {
			path = append(path, '(')
			backtrack(open+1, close)
			path = path[:len(path)-1]
		}
		if close < open {
			path = append(path, ')')
			backtrack(open, close+1)
			path = path[:len(path)-1]
		}
	}

	backtrack(0, 0)
	return result
}
