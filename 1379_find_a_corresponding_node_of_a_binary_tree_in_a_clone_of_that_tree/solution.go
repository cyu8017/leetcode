// LeetCode 1379 - Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getTargetCopy(original *TreeNode, cloned *TreeNode, target *TreeNode) *TreeNode {
	type pair struct{ a, b *TreeNode }
	stack := []pair{{original, cloned}}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if cur.a == target || cur.a.Val == target.Val {
			return cur.b
		}
		if cur.a.Left != nil {
			stack = append(stack, pair{cur.a.Left, cur.b.Left})
		}
		if cur.a.Right != nil {
			stack = append(stack, pair{cur.a.Right, cur.b.Right})
		}
	}
	return nil
}
