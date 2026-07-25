// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

type Node struct {
	Val    int
	Left   *Node
	Right  *Node
	Parent *Node
}

func lowestCommonAncestor(p, q *Node) *Node {
	a, b := p, q
	for a != b {
		if a != nil {
			a = a.Parent
		} else {
			a = q
		}
		if b != nil {
			b = b.Parent
		} else {
			b = p
		}
	}
	return a
}
