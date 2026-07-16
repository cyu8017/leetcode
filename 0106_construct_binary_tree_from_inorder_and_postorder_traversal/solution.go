// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(inorder []int, postorder []int) *TreeNode {
	index := make(map[int]int, len(inorder))
	for i, v := range inorder {
		index[v] = i
	}
	postIndex := len(postorder) - 1

	var build func(left, right int) *TreeNode
	build = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}
		rootVal := postorder[postIndex]
		postIndex--
		mid := index[rootVal]
		root := &TreeNode{Val: rootVal}
		root.Right = build(mid+1, right)
		root.Left = build(left, mid-1)
		return root
	}

	return build(0, len(inorder)-1)
}