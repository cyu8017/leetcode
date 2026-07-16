// LeetCode 0116 - Populating Next Right Pointers in Each Node
type Node struct { Val int; Left, Right, Next *Node }
func connect(root *Node) *Node {
	if root == nil { return nil }; q := []*Node{root}
	for len(q) > 0 { n := len(q); var prev *Node
		for i := 0; i < n; i++ { cur := q[0]; q = q[1:]
			if prev != nil { prev.Next = cur }; prev = cur
			if cur.Left != nil { q = append(q, cur.Left) }; if cur.Right != nil { q = append(q, cur.Right) }
		}
		prev.Next = nil
	}
	return root
}