// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
	left, right := 0, 0
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		l, r := dfs(node.Left), dfs(node.Right)
		if node.Val == x {
			left, right = l, r
		}
		return l + r + 1
	}
	dfs(root)
	parentSide := n - left - right - 1
	best := left
	if right > best {
		best = right
	}
	if parentSide > best {
		best = parentSide
	}
	return best > n/2
}
