// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

import "container/heap"

type pathEdge3970 struct {
	to     int
	weight int
}

type pathState3970 struct {
	distance int64
	node     int
	run      int
}

type pathHeap3970 []pathState3970

func (h pathHeap3970) Len() int           { return len(h) }
func (h pathHeap3970) Less(i, j int) bool { return h[i].distance < h[j].distance }
func (h pathHeap3970) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *pathHeap3970) Push(value any)    { *h = append(*h, value.(pathState3970)) }
func (h *pathHeap3970) Pop() any {
	old := *h
	value := old[len(old)-1]
	*h = old[:len(old)-1]
	return value
}

func shortestPath(n int, edges [][]int, labels string, k int) int64 {
	graph := make([][]pathEdge3970, n)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], pathEdge3970{edge[1], edge[2]})
	}
	const infinity = int64(^uint64(0) >> 2)
	distances := make([][]int64, n)
	for node := range distances {
		distances[node] = make([]int64, k+1)
		for run := 1; run <= k; run++ {
			distances[node][run] = infinity
		}
	}
	distances[0][1] = 0
	queue := &pathHeap3970{{distance: 0, node: 0, run: 1}}
	heap.Init(queue)
	for queue.Len() > 0 {
		current := heap.Pop(queue).(pathState3970)
		if current.distance != distances[current.node][current.run] {
			continue
		}
		if current.node == n-1 {
			return current.distance
		}
		for _, edge := range graph[current.node] {
			nextRun := 1
			if labels[current.node] == labels[edge.to] {
				nextRun = current.run + 1
			}
			if nextRun > k {
				continue
			}
			nextDistance := current.distance + int64(edge.weight)
			if nextDistance < distances[edge.to][nextRun] {
				distances[edge.to][nextRun] = nextDistance
				heap.Push(queue, pathState3970{nextDistance, edge.to, nextRun})
			}
		}
	}
	return -1
}