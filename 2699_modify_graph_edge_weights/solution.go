// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/


import "container/heap"

type ge struct{ to, w, idx int }
type gi struct{ node, dist int }
type gh []gi
func (h gh) Len() int            { return len(h) }
func (h gh) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h gh) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *gh) Push(x interface{}) { *h = append(*h, x.(gi)) }
func (h *gh) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func modifiedGraphEdges(n int, edges [][]int, source int, destination int, target int) [][]int {
	g := make([][]ge, n)
	for i, e := range edges {
		u, v, w := e[0], e[1], e[2]
		g[u] = append(g[u], ge{v, w, i})
		g[v] = append(g[v], ge{u, w, i})
	}
	dijkstra := func(from int, useMod bool) []int {
		dist := make([]int, n)
		for i := range dist {
			dist[i] = int(1e15)
		}
		dist[from] = 0
		h := &gh{{from, 0}}
		heap.Init(h)
		for h.Len() > 0 {
			cur := heap.Pop(h).(gi)
			if cur.dist > dist[cur.node] {
				continue
			}
			for _, e := range g[cur.node] {
				w := e.w
				if w == -1 {
					if useMod {
						w = 1
					} else {
						continue
					}
				}
				nd := cur.dist + w
				if nd < dist[e.to] {
					dist[e.to] = nd
					heap.Push(h, gi{e.to, nd})
				}
			}
		}
		return dist
	}
	distToDest := dijkstra(source, false)
	if distToDest[destination] < target {
		return [][]int{}
	}
	if distToDest[destination] == target {
		for i := range edges {
			if edges[i][2] == -1 {
				edges[i][2] = int(2e9)
			}
		}
		return edges
	}
	distFromDest := dijkstra(destination, true)
	_ = distFromDest
	for i, e := range edges {
		if e[2] != -1 {
			continue
		}
		u, v := e[0], e[1]
		// set weight so that path can reach target
		w := target - distToDest[u] - distFromDest[v]
		if w < 1 {
			w = target - distToDest[v] - distFromDest[u]
		}
		if w < 1 {
			w = 1
		}
		edges[i][2] = w
		g[u] = append([]ge{}, g[u]...) // refresh? weights stored in edges; rebuild needed
	}
	// rebuild graph with updated weights and verify via constructive approach
	for i := range edges {
		if edges[i][2] == -1 {
			edges[i][2] = 1
		}
	}
	// Standard algorithm
	return modifiedGraphEdgesCorrect(n, edges, source, destination, target)
}

func modifiedGraphEdgesCorrect(n int, edges [][]int, source, destination, target int) [][]int {
	const INF = int(2e9)
	g := make([][][3]int, n) // to, wptr idx, isNeg
	for i, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], [3]int{v, i, 0})
		g[v] = append(g[v], [3]int{u, i, 0})
	}
	dijkstra := func(ignoreNeg bool) []int {
		dist := make([]int, n)
		for i := range dist {
			dist[i] = INF
		}
		dist[source] = 0
		h := &gh{{source, 0}}
		heap.Init(h)
		for h.Len() > 0 {
			cur := heap.Pop(h).(gi)
			if cur.dist != dist[cur.node] {
				continue
			}
			for _, it := range g[cur.node] {
				to, idx := it[0], it[1]
				w := edges[idx][2]
				if w == -1 {
					if ignoreNeg {
						continue
					}
					w = 1
				}
				if cur.dist+w < dist[to] {
					dist[to] = cur.dist + w
					heap.Push(h, gi{to, dist[to]})
				}
			}
		}
		return dist
	}
	d := dijkstra(true)
	if d[destination] < target {
		return [][]int{}
	}
	matched := d[destination] == target
	for i := range edges {
		if edges[i][2] != -1 {
			continue
		}
		if matched {
			edges[i][2] = INF
			continue
		}
		edges[i][2] = 1
		d = dijkstra(false)
		if d[destination] <= target {
			edges[i][2] += target - d[destination]
			matched = true
		}
	}
	d = dijkstra(false)
	if d[destination] != target {
		return [][]int{}
	}
	return edges
}
