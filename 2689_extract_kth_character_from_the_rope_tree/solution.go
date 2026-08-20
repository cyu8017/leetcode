// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/


type RopeTreeNode struct {
	Len   int
	Val   byte
	Left  *RopeTreeNode
	Right *RopeTreeNode
}

func getKthCharacter(root *RopeTreeNode, k int) byte {
	var dfs func(*RopeTreeNode, int) byte
	dfs = func(node *RopeTreeNode, kk int) byte {
		if node.Left == nil && node.Right == nil {
			return node.Val
		}
		leftLen := 0
		if node.Left != nil {
			if node.Left.Len > 0 {
				leftLen = node.Left.Len
			} else {
				leftLen = 1
			}
		}
		if kk <= leftLen {
			return dfs(node.Left, kk)
		}
		return dfs(node.Right, kk-leftLen)
	}
	return dfs(root, k)
}
