// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

type Node struct {
	Val      int
	Children []*Node
}

func findRoot(tree []*Node) *Node {
	value := 0
	nodes := map[int]*Node{}
	for _, node := range tree {
		nodes[node.Val] = node
		value ^= node.Val
		for _, child := range node.Children {
			value ^= child.Val
		}
	}
	return nodes[value]
}
