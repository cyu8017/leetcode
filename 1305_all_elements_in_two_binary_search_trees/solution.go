// LeetCode 1305 - All Elements in Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	inorder := func(root *TreeNode) []int {
		var result []int
		var dfs func(*TreeNode)
		dfs = func(node *TreeNode) {
			if node == nil {
				return
			}
			dfs(node.Left)
			result = append(result, node.Val)
			dfs(node.Right)
		}
		dfs(root)
		return result
	}
	a, b := inorder(root1), inorder(root2)
	answer := make([]int, 0, len(a)+len(b))
	i, j := 0, 0
	for i < len(a) || j < len(b) {
		if j == len(b) || (i < len(a) && a[i] <= b[j]) {
			answer = append(answer, a[i])
			i++
		} else {
			answer = append(answer, b[j])
			j++
		}
	}
	return answer
}
