// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func smallestFromLeaf(root *TreeNode) string {
	best := "~"
	var dfs func(*TreeNode, string)
	dfs = func(node *TreeNode, path string) {
		if node == nil {
			return
		}
		path = string(rune('a'+node.Val)) + path
		if node.Left == nil && node.Right == nil {
			if path < best {
				best = path
			}
			return
		}
		dfs(node.Left, path)
		dfs(node.Right, path)
	}
	dfs(root, "")
	return best
}
