// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

import "container/heap"

type pqItem struct{ moves, node int }
type maxPQ []pqItem

func (h maxPQ) Len() int            { return len(h) }
func (h maxPQ) Less(i, j int) bool  { return h[i].moves > h[j].moves }
func (h maxPQ) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxPQ) Push(x interface{}) { *h = append(*h, x.(pqItem)) }
func (h *maxPQ) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func reachableNodes(edges [][]int, maxMoves int, n int) int {
	graph := make([]map[int]int, n)
	for i := range graph {
		graph[i] = map[int]int{}
	}
	for _, e := range edges {
		u, v, cnt := e[0], e[1], e[2]
		graph[u][v] = cnt
		graph[v][u] = cnt
	}
	pq := &maxPQ{{maxMoves, 0}}
	heap.Init(pq)
	seen := map[int]int{}
	for pq.Len() > 0 {
		cur := heap.Pop(pq).(pqItem)
		if _, ok := seen[cur.node]; ok {
			continue
		}
		seen[cur.node] = cur.moves
		for nei, cnt := range graph[cur.node] {
			remain := cur.moves - cnt - 1
			if _, ok := seen[nei]; !ok && remain >= 0 {
				heap.Push(pq, pqItem{remain, nei})
			}
		}
	}
	ans := len(seen)
	for _, e := range edges {
		u, v, cnt := e[0], e[1], e[2]
		reach := seen[u] + seen[v]
		if reach > cnt {
			reach = cnt
		}
		ans += reach
	}
	return ans
}
