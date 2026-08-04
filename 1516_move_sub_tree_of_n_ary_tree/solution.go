// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

type Node struct {
	Val      int
	Children []*Node
}

func moveSubTree(root *Node, p *Node, q *Node) *Node {
	parent := map[*Node]*Node{}
	var build func(*Node)
	build = func(node *Node) {
		for _, child := range node.Children {
			parent[child] = node
			build(child)
		}
	}
	build(root)
	if parent[p] == q {
		return root
	}
	isAncestor := func(a, b *Node) bool {
		cur := b
		for {
			par, ok := parent[cur]
			if !ok {
				return false
			}
			if par == a {
				return true
			}
			cur = par
		}
	}
	removeChild := func(par, child *Node) {
		for i, c := range par.Children {
			if c == child {
				par.Children = append(par.Children[:i], par.Children[i+1:]...)
				return
			}
		}
	}
	replaceChild := func(par, old, neu *Node) {
		for i, c := range par.Children {
			if c == old {
				par.Children[i] = neu
				return
			}
		}
	}
	pParent := parent[p]
	qParent := parent[q]
	if isAncestor(p, q) {
		removeChild(qParent, q)
		if pParent == nil {
			root = q
		} else {
			replaceChild(pParent, p, q)
		}
		q.Children = append(q.Children, p)
	} else {
		if pParent == nil {
			root = q
		} else {
			removeChild(pParent, p)
		}
		q.Children = append(q.Children, p)
	}
	return root
}
