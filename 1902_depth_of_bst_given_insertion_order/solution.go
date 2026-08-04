// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

import "sort"

func maxDepthBST(order []int) int {
	type node struct {
		value, depth int
	}
	nodes := make([]node, 0, len(order))
	ans := 0
	for _, value := range order {
		i := sort.Search(len(nodes), func(j int) bool {
			return nodes[j].value >= value
		})
		depth := 1
		if i > 0 && nodes[i-1].depth+1 > depth {
			depth = nodes[i-1].depth + 1
		}
		if i < len(nodes) && nodes[i].depth+1 > depth {
			depth = nodes[i].depth + 1
		}
		nodes = append(nodes, node{})
		copy(nodes[i+1:], nodes[i:])
		nodes[i] = node{value: value, depth: depth}
		if depth > ans {
			ans = depth
		}
	}
	return ans
}
