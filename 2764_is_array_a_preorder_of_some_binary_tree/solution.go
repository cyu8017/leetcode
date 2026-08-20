// LeetCode 2764 - Is Array a Preorder of Some ‌Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

func isPreorder(nodes [][]int) bool {
	if len(nodes) == 0 {
		return true
	}
	stack := []int{nodes[0][0]}
	for i := 1; i < len(nodes); i++ {
		id, parent := nodes[i][0], nodes[i][1]
		for len(stack) > 0 && stack[len(stack)-1] != parent {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			return false
		}
		stack = append(stack, id)
	}
	return true
}
