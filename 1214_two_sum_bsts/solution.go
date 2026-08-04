// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func twoSumBSTs(root1 *TreeNode, root2 *TreeNode, target int) bool {
	values := map[int]bool{}
	stack := []*TreeNode{}
	if root1 != nil {
		stack = append(stack, root1)
	}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		values[node.Val] = true
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	stack = nil
	if root2 != nil {
		stack = append(stack, root2)
	}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if values[target-node.Val] {
			return true
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	return false
}
