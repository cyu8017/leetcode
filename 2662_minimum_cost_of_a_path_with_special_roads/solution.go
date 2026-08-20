// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/


import "container/heap"

type nodeCost struct{ id, cost int }
type costH []nodeCost
func (h costH) Len() int            { return len(h) }
func (h costH) Less(i, j int) bool  { return h[i].cost < h[j].cost }
func (h costH) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *costH) Push(x interface{}) { *h = append(*h, x.(nodeCost)) }
func (h *costH) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minimumCost(start []int, target []int, specialRoads [][]int) int {
	points := [][]int{start, target}
	for _, r := range specialRoads {
		points = append(points, []int{r[0], r[1]}, []int{r[2], r[3]})
	}
	N := len(points)
	distMan := func(a, b []int) int {
		dx, dy := a[0]-b[0], a[1]-b[1]
		if dx < 0 {
			dx = -dx
		}
		if dy < 0 {
			dy = -dy
		}
		return dx + dy
	}
	g := make([][]nodeCost, N)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if i != j {
				g[i] = append(g[i], nodeCost{j, distMan(points[i], points[j])})
			}
		}
	}
	for _, r := range specialRoads {
		u, v := -1, -1
		for i, p := range points {
			if p[0] == r[0] && p[1] == r[1] {
				u = i
			}
			if p[0] == r[2] && p[1] == r[3] {
				v = i
			}
		}
		if u >= 0 && v >= 0 {
			g[u] = append(g[u], nodeCost{v, r[4]})
		}
	}
	dist := make([]int, N)
	for i := range dist {
		dist[i] = 1 << 30
	}
	dist[0] = 0
	h := &costH{{0, 0}}
	heap.Init(h)
	for h.Len() > 0 {
		cur := heap.Pop(h).(nodeCost)
		if cur.cost > dist[cur.id] {
			continue
		}
		for _, e := range g[cur.id] {
			nd := cur.cost + e.cost
			if nd < dist[e.id] {
				dist[e.id] = nd
				heap.Push(h, nodeCost{e.id, nd})
			}
		}
	}
	return dist[1]
}
