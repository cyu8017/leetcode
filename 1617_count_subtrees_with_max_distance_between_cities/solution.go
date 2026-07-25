// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

func countSubgraphsForEachDiameter(n int, edges [][]int) []int {
	adj := make([][]int, n)
	for _, e := range edges {
		a, b := e[0]-1, e[1]-1
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	ans := make([]int, n-1)
	bfs := func(mask, src int) (int, map[int]int) {
		dist := map[int]int{src: 0}
		q := []int{src}
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			for _, v := range adj[u] {
				if mask>>v&1 == 1 {
					if _, ok := dist[v]; !ok {
						dist[v] = dist[u] + 1
						q = append(q, v)
					}
				}
			}
		}
		far := src
		for node, d := range dist {
			if d > dist[far] {
				far = node
			}
		}
		return far, dist
	}
	bitCount := func(x int) int {
		c := 0
		for x > 0 {
			c++
			x &= x - 1
		}
		return c
	}
	for mask := 1; mask < 1<<n; mask++ {
		if mask&(mask-1) == 0 {
			continue
		}
		start := 0
		for (mask>>start)&1 == 0 {
			start++
		}
		far, seen := bfs(mask, start)
		if len(seen) == bitCount(mask) {
			_, dist := bfs(mask, far)
			mx := 0
			for _, d := range dist {
				if d > mx {
					mx = d
				}
			}
			ans[mx-1]++
		}
	}
	return ans
}
