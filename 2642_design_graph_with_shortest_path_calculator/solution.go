// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/


import "container/heap"

type edge struct{ to, w int }
type Graph struct {
	g [][]edge
}

func Constructor(n int, edges [][]int) Graph {
	g := make([][]edge, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], edge{e[1], e[2]})
	}
	return Graph{g: g}
}

func (this *Graph) AddEdge(edgeArr []int) {
	this.g[edgeArr[0]] = append(this.g[edgeArr[0]], edge{edgeArr[1], edgeArr[2]})
}

type dijkItem struct{ node, dist int }
type dijkH []dijkItem
func (h dijkH) Len() int            { return len(h) }
func (h dijkH) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h dijkH) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *dijkH) Push(x interface{}) { *h = append(*h, x.(dijkItem)) }
func (h *dijkH) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func (this *Graph) ShortestPath(node1 int, node2 int) int {
	n := len(this.g)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = 1 << 30
	}
	dist[node1] = 0
	h := &dijkH{{node1, 0}}
	heap.Init(h)
	for h.Len() > 0 {
		cur := heap.Pop(h).(dijkItem)
		if cur.node == node2 {
			return cur.dist
		}
		if cur.dist > dist[cur.node] {
			continue
		}
		for _, e := range this.g[cur.node] {
			nd := cur.dist + e.w
			if nd < dist[e.to] {
				dist[e.to] = nd
				heap.Push(h, dijkItem{e.to, nd})
			}
		}
	}
	return -1
}
