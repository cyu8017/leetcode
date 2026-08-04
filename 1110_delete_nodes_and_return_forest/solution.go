// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	deleteSet := map[int]bool{}
	for _, v := range to_delete {
		deleteSet[v] = true
	}
	forest := []*TreeNode{}
	var dfs func(*TreeNode, bool) *TreeNode
	dfs = func(node *TreeNode, isRoot bool) *TreeNode {
		if node == nil {
			return nil
		}
		removed := deleteSet[node.Val]
		if isRoot && !removed {
			forest = append(forest, node)
		}
		node.Left = dfs(node.Left, removed)
		node.Right = dfs(node.Right, removed)
		if removed {
			return nil
		}
		return node
	}
	dfs(root, true)
	return forest
}
