// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func widthOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	type item struct {
		node *TreeNode
		idx  int
	}
	queue := []item{{root, 0}}
	best := 0
	for len(queue) > 0 {
		left := queue[0].idx
		size := len(queue)
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]
			if cur.idx-left+1 > best {
				best = cur.idx - left + 1
			}
			if cur.node.Left != nil {
				queue = append(queue, item{cur.node.Left, cur.idx * 2})
			}
			if cur.node.Right != nil {
				queue = append(queue, item{cur.node.Right, cur.idx*2 + 1})
			}
		}
	}
	return best
}
