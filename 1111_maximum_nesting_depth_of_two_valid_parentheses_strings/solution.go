// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

func maxDepthAfterSplit(seq string) []int {
	depth := 0
	ans := make([]int, len(seq))
	for i := 0; i < len(seq); i++ {
		if seq[i] == '(' {
			ans[i] = depth % 2
			depth++
		} else {
			depth--
			ans[i] = depth % 2
		}
	}
	return ans
}
