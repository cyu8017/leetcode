// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

type Node struct {
	Val      int
	Children []*Node
}

func diameter(root *Node) int {
	answer := 0
	var depth func(*Node) int
	depth = func(node *Node) int {
		longest, second := 0, 0
		for _, child := range node.Children {
			value := depth(child) + 1
			if value > longest {
				longest, second = value, longest
			} else if value > second {
				second = value
			}
		}
		if longest+second > answer {
			answer = longest + second
		}
		return longest
	}
	if root != nil {
		depth(root)
	}
	return answer
}
