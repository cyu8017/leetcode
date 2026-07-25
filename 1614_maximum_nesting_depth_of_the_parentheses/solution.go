// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

func maxDepth(s string) int {
	depth, ans := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			depth++
			if depth > ans {
				ans = depth
			}
		} else if s[i] == ')' {
			depth--
		}
	}
	return ans
}
