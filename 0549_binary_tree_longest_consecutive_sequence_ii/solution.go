// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestConsecutive(root *TreeNode) int {
	best := 0

	var dfs func(node *TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}

		leftInc, leftDec := dfs(node.Left)
		rightInc, rightDec := dfs(node.Right)

		inc := 1
		dec := 1
		if node.Left != nil {
			if node.Left.Val == node.Val+1 {
				if leftInc+1 > inc {
					inc = leftInc + 1
				}
			} else if node.Left.Val == node.Val-1 {
				if leftDec+1 > dec {
					dec = leftDec + 1
				}
			}
		}
		if node.Right != nil {
			if node.Right.Val == node.Val+1 {
				if rightInc+1 > inc {
					inc = rightInc + 1
				}
			} else if node.Right.Val == node.Val-1 {
				if rightDec+1 > dec {
					dec = rightDec + 1
				}
			}
		}

		if node.Left != nil && node.Right != nil {
			if node.Left.Val+1 == node.Val && node.Val+1 == node.Right.Val {
				if leftDec+1+rightInc > best {
					best = leftDec + 1 + rightInc
				}
			}
			if node.Left.Val-1 == node.Val && node.Val-1 == node.Right.Val {
				if leftInc+1+rightDec > best {
					best = leftInc + 1 + rightDec
				}
			}
		}

		if inc > best {
			best = inc
		}
		if dec > best {
			best = dec
		}
		return inc, dec
	}

	dfs(root)
	return best
}
