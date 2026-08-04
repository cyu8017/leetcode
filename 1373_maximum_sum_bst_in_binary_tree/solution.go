// LeetCode 1373 - Maximum Sum BST in Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxSumBST(root *TreeNode) int {
	ans := 0
	const inf = int(1e9)
	var dfs func(*TreeNode) (bool, int, int, int)
	dfs = func(node *TreeNode) (bool, int, int, int) {
		if node == nil {
			return true, inf, -inf, 0
		}
		a, lx, lh, ls := dfs(node.Left)
		b, rx, rh, rs := dfs(node.Right)
		if a && b && lh < node.Val && node.Val < rx {
			s := ls + rs + node.Val
			if s > ans {
				ans = s
			}
			mn, mx := node.Val, node.Val
			if lx < mn {
				mn = lx
			}
			if rh > mx {
				mx = rh
			}
			return true, mn, mx, s
		}
		return false, 0, 0, 0
	}
	dfs(root)
	return ans
}
