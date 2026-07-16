// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	index := make(map[int]int, len(inorder))
	for i, v := range inorder {
		index[v] = i
	}
	preIndex := 0

	var build func(left, right int) *TreeNode
	build = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}
		rootVal := preorder[preIndex]
		preIndex++
		mid := index[rootVal]
		root := &TreeNode{Val: rootVal}
		root.Left = build(left, mid-1)
		root.Right = build(mid+1, right)
		return root
	}

	return build(0, len(inorder)-1)
}