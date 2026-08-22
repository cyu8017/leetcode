// LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

func interactionCost(n int, edges [][]int, group []int) int64 {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	total := [21]int{}
	for _, x := range group {
		total[x]++
	}
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -2
	}
	parent[0] = -1
	order := []int{0}
	for i := 0; i < len(order); i++ {
		u := order[i]
		for _, v := range g[u] {
			if parent[v] == -2 {
				parent[v] = u
				order = append(order, v)
			}
		}
	}
	count := make([][21]int, n)
	var ans int64
	for i := n - 1; i >= 0; i-- {
		u := order[i]
		count[u][group[u]]++
		for _, v := range g[u] {
			if parent[v] != u {
				continue
			}
			for c := 1; c <= 20; c++ {
				x := count[v][c]
				ans += int64(x * (total[c] - x))
				count[u][c] += x
			}
		}
	}
	return ans
}