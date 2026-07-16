// LeetCode 0133 - Clone Graph
type Node struct {
	Val int
	Neighbors []*Node
}
func cloneGraph(node *Node) *Node {
	if node == nil { return nil }
	copies := make(map[*Node]*Node)
	var dfs func(*Node) *Node
	dfs = func(current *Node) *Node {
		if copy, ok := copies[current]; ok { return copy }
		copy := &Node{Val: current.Val}
		copies[current] = copy
		for _, neighbor := range current.Neighbors { copy.Neighbors = append(copy.Neighbors, dfs(neighbor)) }
		return copy
	}
	return dfs(node)
}