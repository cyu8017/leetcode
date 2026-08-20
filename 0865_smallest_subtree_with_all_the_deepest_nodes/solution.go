// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
	var dfs func(node *TreeNode) (int, *TreeNode)
	dfs = func(node *TreeNode) (int, *TreeNode) {
		if node == nil {
			return 0, nil
		}
		ld, ln := dfs(node.Left)
		rd, rn := dfs(node.Right)
		if ld > rd {
			return ld + 1, ln
		}
		if rd > ld {
			return rd + 1, rn
		}
		return ld + 1, node
	}
	_, ans := dfs(root)
	return ans
}
