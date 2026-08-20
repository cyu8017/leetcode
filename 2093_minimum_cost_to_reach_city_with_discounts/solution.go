// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

import "container/heap"

type item2093 struct{ cost, city, disc int }
type pq2093 []item2093

func (p pq2093) Len() int            { return len(p) }
func (p pq2093) Less(i, j int) bool  { return p[i].cost < p[j].cost }
func (p pq2093) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *pq2093) Push(x interface{}) { *p = append(*p, x.(item2093)) }
func (p *pq2093) Pop() interface{} {
	old := *p
	x := old[len(old)-1]
	*p = old[:len(old)-1]
	return x
}

func minimumCost(n int, highways [][]int, discounts int) int {
	g := make([][][2]int, n)
	for _, h := range highways {
		g[h[0]] = append(g[h[0]], [2]int{h[1], h[2]})
		g[h[1]] = append(g[h[1]], [2]int{h[0], h[2]})
	}
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, discounts+1)
		for j := range dist[i] {
			dist[i][j] = 1 << 30
		}
	}
	h := &pq2093{{0, 0, discounts}}
	heap.Init(h)
	dist[0][discounts] = 0
	for h.Len() > 0 {
		cur := heap.Pop(h).(item2093)
		if cur.city == n-1 {
			return cur.cost
		}
		if cur.cost > dist[cur.city][cur.disc] {
			continue
		}
		for _, e := range g[cur.city] {
			v, w := e[0], e[1]
			if cur.cost+w < dist[v][cur.disc] {
				dist[v][cur.disc] = cur.cost + w
				heap.Push(h, item2093{dist[v][cur.disc], v, cur.disc})
			}
			if cur.disc > 0 && cur.cost+w/2 < dist[v][cur.disc-1] {
				dist[v][cur.disc-1] = cur.cost + w/2
				heap.Push(h, item2093{dist[v][cur.disc-1], v, cur.disc - 1})
			}
		}
	}
	return -1
}
