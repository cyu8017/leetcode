// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

type dsu struct {
	parent     []int
	components int
}

func newDSU(n int) *dsu {
	parent := make([]int, n+1)
	for i := range parent {
		parent[i] = i
	}
	return &dsu{parent: parent, components: n}
}

func (d *dsu) find(x int) int {
	for x != d.parent[x] {
		d.parent[x] = d.parent[d.parent[x]]
		x = d.parent[x]
	}
	return x
}

func (d *dsu) union(a, b int) bool {
	a, b = d.find(a), d.find(b)
	if a == b {
		return false
	}
	d.parent[a] = b
	d.components--
	return true
}

func maxNumEdgesToRemove(n int, edges [][]int) int {
	alice, bob, used := newDSU(n), newDSU(n), 0
	for _, e := range edges {
		t, u, v := e[0], e[1], e[2]
		if t == 3 {
			merged := alice.union(u, v)
			bob.union(u, v)
			if merged {
				used++
			}
		}
	}
	for _, e := range edges {
		t, u, v := e[0], e[1], e[2]
		if t == 1 {
			if alice.union(u, v) {
				used++
			}
		} else if t == 2 {
			if bob.union(u, v) {
				used++
			}
		}
	}
	if alice.components == 1 && bob.components == 1 {
		return len(edges) - used
	}
	return -1
}
