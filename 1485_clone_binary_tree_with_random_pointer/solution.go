// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

type Node struct {
	Val    int
	Left   *Node
	Right  *Node
	Random *Node
}

func copyRandomBinaryTree(root *Node) *Node {
	copies := map[*Node]*Node{}
	var clone func(*Node) *Node
	clone = func(node *Node) *Node {
		if node == nil {
			return nil
		}
		if c, ok := copies[node]; ok {
			return c
		}
		copies[node] = &Node{Val: node.Val}
		copies[node].Left = clone(node.Left)
		copies[node].Right = clone(node.Right)
		copies[node].Random = clone(node.Random)
		return copies[node]
	}
	return clone(root)
}
