// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type FindElements struct {
	values map[int]bool
}

func Constructor(root *TreeNode) FindElements {
	fe := FindElements{values: map[int]bool{}}
	var recover func(*TreeNode, int)
	recover = func(node *TreeNode, value int) {
		if node == nil {
			return
		}
		node.Val = value
		fe.values[value] = true
		recover(node.Left, 2*value+1)
		recover(node.Right, 2*value+2)
	}
	recover(root, 0)
	return fe
}

func (this *FindElements) Find(target int) bool {
	return this.values[target]
}
