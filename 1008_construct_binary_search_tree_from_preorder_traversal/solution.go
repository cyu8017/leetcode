// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func bstFromPreorder(preorder []int) *TreeNode {
	i := 0
	var build func(bound int) *TreeNode
	build = func(bound int) *TreeNode {
		if i == len(preorder) || preorder[i] > bound {
			return nil
		}
		root := &TreeNode{Val: preorder[i]}
		i++
		root.Left = build(root.Val)
		root.Right = build(bound)
		return root
	}
	return build(1 << 30)
}
