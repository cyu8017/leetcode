// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countPairs(root *TreeNode, distance int) int {
	answer := 0
	var dfs func(*TreeNode) []int
	dfs = func(node *TreeNode) []int {
		if node == nil {
			return nil
		}
		if node.Left == nil && node.Right == nil {
			return []int{1}
		}
		left, right := dfs(node.Left), dfs(node.Right)
		for _, a := range left {
			for _, b := range right {
				if a+b <= distance {
					answer++
				}
			}
		}
		out := []int{}
		for _, depth := range append(left, right...) {
			if depth+1 < distance {
				out = append(out, depth+1)
			}
		}
		return out
	}
	dfs(root)
	return answer
}
