// LeetCode 0138 - Copy List with Random Pointer
type Node struct {
	Val int
	Next *Node
	Random *Node
}
func copyRandomList(head *Node) *Node {
	if head == nil { return nil }
	copies := make(map[*Node]*Node)
	for node := head; node != nil; node = node.Next { copies[node] = &Node{Val: node.Val} }
	for node := head; node != nil; node = node.Next {
		copies[node].Next = copies[node.Next]
		copies[node].Random = copies[node.Random]
	}
	return copies[head]
}