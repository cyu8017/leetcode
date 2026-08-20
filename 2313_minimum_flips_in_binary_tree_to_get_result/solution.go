// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minimumFlips(root *TreeNode, result bool) int {
	var dfs func(*TreeNode) (int, int) // cost to make false, true
	dfs = func(node *TreeNode) (int, int) {
		if node.Left == nil && node.Right == nil {
			if node.Val == 0 {
				return 0, 1
			}
			return 1, 0
		}
		if node.Val == 5 { // NOT
			f, t := dfs(node.Left)
			return t, f
		}
		lf, lt := dfs(node.Left)
		rf, rt := dfs(node.Right)
		switch node.Val {
		case 2: // OR
			return lf + rf, min4(lt+rt, lt+rf, lf+rt)
		case 3: // AND
			return min4(lf+rf, lf+rt, lt+rf), lt + rt
		case 4: // XOR
			return min(lf+rf, lt+rt), min(lf+rt, lt+rf)
		}
		return 0, 0
	}
	f, t := dfs(root)
	if result {
		return t
	}
	return f
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func min4(a, b, c int) int {
	if b < a {
		a = b
	}
	if c < a {
		a = c
	}
	return a
}
