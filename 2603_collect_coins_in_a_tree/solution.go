// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/


func collectTheCoins(coins []int, edges [][]int) int {
	n := len(coins)
	g := make([]map[int]bool, n)
	for i := range g {
		g[i] = map[int]bool{}
	}
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u][v] = true
		g[v][u] = true
	}
	deg := make([]int, n)
	for i := 0; i < n; i++ {
		deg[i] = len(g[i])
	}
	q := []int{}
	for i := 0; i < n; i++ {
		if deg[i] == 1 && coins[i] == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for v := range g[u] {
			delete(g[v], u)
			deg[v]--
			if deg[v] == 1 && coins[v] == 0 {
				q = append(q, v)
			}
		}
		g[u] = map[int]bool{}
		deg[u] = 0
	}
	for round := 0; round < 2; round++ {
		leaves := []int{}
		for i := 0; i < n; i++ {
			if deg[i] == 1 {
				leaves = append(leaves, i)
			}
		}
		for _, u := range leaves {
			for v := range g[u] {
				delete(g[v], u)
				deg[v]--
			}
			g[u] = map[int]bool{}
			deg[u] = 0
		}
	}
	remain := 0
	for i := 0; i < n; i++ {
		remain += len(g[i])
	}
	return remain
}
