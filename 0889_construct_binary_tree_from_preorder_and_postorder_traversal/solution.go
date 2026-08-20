// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func constructFromPrePost(preorder []int, postorder []int) *TreeNode {
	postIndex := map[int]int{}
	for i, v := range postorder {
		postIndex[v] = i
	}
	var build func(preLo, preHi, postLo, postHi int) *TreeNode
	build = func(preLo, preHi, postLo, postHi int) *TreeNode {
		if preLo > preHi {
			return nil
		}
		root := &TreeNode{Val: preorder[preLo]}
		if preLo == preHi {
			return root
		}
		leftVal := preorder[preLo+1]
		leftPost := postIndex[leftVal]
		leftSize := leftPost - postLo + 1
		root.Left = build(preLo+1, preLo+leftSize, postLo, leftPost)
		root.Right = build(preLo+leftSize+1, preHi, leftPost+1, postHi-1)
		return root
	}
	n := len(preorder)
	return build(0, n-1, 0, n-1)
}
