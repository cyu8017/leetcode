// LeetCode 1339 - Maximum Product of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxProduct(root *TreeNode) int {
	var sums []int64
	var total func(*TreeNode) int64
	total = func(node *TreeNode) int64 {
		if node == nil {
			return 0
		}
		value := int64(node.Val) + total(node.Left) + total(node.Right)
		sums = append(sums, value)
		return value
	}
	whole := total(root)
	var best int64
	for _, value := range sums {
		prod := value * (whole - value)
		if prod > best {
			best = prod
		}
	}
	return int(best % 1000000007)
}
