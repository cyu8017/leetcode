// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

import "container/list"

func minThreshold(n int, edges [][]int, source int, target int, k int) int {
	if source == target {
		return 0
	}
	type edge3924 struct{ to, weight int }
	g := make([][]edge3924, n)
	maxWeight := 0
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], edge3924{e[1], e[2]})
		g[e[1]] = append(g[e[1]], edge3924{e[0], e[2]})
		if e[2] > maxWeight {
			maxWeight = e[2]
		}
	}
	can := func(threshold int) bool {
		const inf = int(1e9)
		dist := make([]int, n)
		for i := range dist {
			dist[i] = inf
		}
		dist[source] = 0
		deque := list.New()
		deque.PushBack(source)
		for deque.Len() > 0 {
			front := deque.Front()
			u := front.Value.(int)
			deque.Remove(front)
			for _, e := range g[u] {
				cost := 0
				if e.weight > threshold {
					cost = 1
				}
				if dist[u]+cost >= dist[e.to] || dist[u]+cost > k {
					continue
				}
				dist[e.to] = dist[u] + cost
				if cost == 0 {
					deque.PushFront(e.to)
				} else {
					deque.PushBack(e.to)
				}
			}
		}
		return dist[target] <= k
	}
	if !can(maxWeight) {
		return -1
	}
	lo, hi := 0, maxWeight
	for lo < hi {
		mid := lo + (hi-lo)/2
		if can(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}