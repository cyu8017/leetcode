// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

import "sort"

func countRestrictedPaths(n int, edges [][]int) int {
	type pair struct{ node, weight int }
	adj := make([][]pair, n+1)
	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], pair{e[1], e[2]})
		adj[e[1]] = append(adj[e[1]], pair{e[0], e[2]})
	}
	const inf = int(1) << 62
	dist := make([]int, n+1)
	for i := range dist {
		dist[i] = inf
	}
	dist[n] = 0
	heapDist := []int{0}
	heapNode := []int{n}
	push := func(d, u int) {
		heapDist = append(heapDist, d)
		heapNode = append(heapNode, u)
		i := len(heapDist) - 1
		for i > 0 {
			parent := (i - 1) / 2
			if heapDist[parent] <= heapDist[i] {
				break
			}
			heapDist[parent], heapDist[i] = heapDist[i], heapDist[parent]
			heapNode[parent], heapNode[i] = heapNode[i], heapNode[parent]
			i = parent
		}
	}
	pop := func() (int, int) {
		d, u := heapDist[0], heapNode[0]
		last := len(heapDist) - 1
		heapDist[0], heapNode[0] = heapDist[last], heapNode[last]
		heapDist, heapNode = heapDist[:last], heapNode[:last]
		i := 0
		for {
			smallest := i
			l, r := 2*i+1, 2*i+2
			if l < len(heapDist) && heapDist[l] < heapDist[smallest] {
				smallest = l
			}
			if r < len(heapDist) && heapDist[r] < heapDist[smallest] {
				smallest = r
			}
			if smallest == i {
				break
			}
			heapDist[i], heapDist[smallest] = heapDist[smallest], heapDist[i]
			heapNode[i], heapNode[smallest] = heapNode[smallest], heapNode[i]
			i = smallest
		}
		return d, u
	}
	for len(heapDist) > 0 {
		d, u := pop()
		if d != dist[u] {
			continue
		}
		for _, vw := range adj[u] {
			nd := d + vw.weight
			if nd < dist[vw.node] {
				dist[vw.node] = nd
				push(nd, vw.node)
			}
		}
	}
	order := make([]int, n)
	for i := range order {
		order[i] = i + 1
	}
	sort.Slice(order, func(a, b int) bool { return dist[order[a]] < dist[order[b]] })
	const mod = 1_000_000_007
	cnt := make([]int, n+1)
	cnt[n] = 1
	for _, u := range order {
		if u == n {
			continue
		}
		for _, vw := range adj[u] {
			if dist[u] > dist[vw.node] {
				cnt[u] = (cnt[u] + cnt[vw.node]) % mod
			}
		}
	}
	return cnt[1]
}
