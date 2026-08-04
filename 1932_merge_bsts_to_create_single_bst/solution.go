// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func canMerge(trees []*TreeNode) *TreeNode {
	valueToRoot := make(map[int]*TreeNode)
	count := make(map[int]int)
	for _, tree := range trees {
		valueToRoot[tree.Val] = tree
		count[tree.Val]++
		if tree.Left != nil {
			count[tree.Left.Val]++
		}
		if tree.Right != nil {
			count[tree.Right.Val]++
		}
	}
	var roots []*TreeNode
	for _, t := range trees {
		if count[t.Val] == 1 {
			roots = append(roots, t)
		}
	}
	if len(roots) != 1 {
		return nil
	}
	root := roots[0]
	delete(valueToRoot, root.Val)

	var merge func(node *TreeNode) bool
	merge = func(node *TreeNode) bool {
		if node == nil {
			return true
		}
		if node.Left != nil {
			if t, ok := valueToRoot[node.Left.Val]; ok {
				node.Left = t
				delete(valueToRoot, t.Val)
			}
		}
		if node.Right != nil {
			if t, ok := valueToRoot[node.Right.Val]; ok {
				node.Right = t
				delete(valueToRoot, t.Val)
			}
		}
		return merge(node.Left) && merge(node.Right)
	}
	if !merge(root) || len(valueToRoot) > 0 {
		return nil
	}

	var isValidBST func(node *TreeNode, lo, hi int, loOK, hiOK bool) bool
	isValidBST = func(node *TreeNode, lo, hi int, loOK, hiOK bool) bool {
		if node == nil {
			return true
		}
		if loOK && !(lo < node.Val) {
			return false
		}
		if hiOK && !(node.Val < hi) {
			return false
		}
		return isValidBST(node.Left, lo, node.Val, loOK, true) &&
			isValidBST(node.Right, node.Val, hi, true, hiOK)
	}
	if !isValidBST(root, 0, 0, false, false) {
		return nil
	}
	return root
}
