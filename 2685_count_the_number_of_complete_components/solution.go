// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/


func countCompleteComponents(n int, edges [][]int) int {
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	seen := make([]bool, n)
	ans := 0
	for i := 0; i < n; i++ {
		if seen[i] {
			continue
		}
		stack := []int{i}
		seen[i] = true
		nodes := []int{}
		edgeCnt := 0
		for len(stack) > 0 {
			u := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			nodes = append(nodes, u)
			edgeCnt += len(g[u])
			for _, v := range g[u] {
				if !seen[v] {
					seen[v] = true
					stack = append(stack, v)
				}
			}
		}
		sz := len(nodes)
		if edgeCnt/2 == sz*(sz-1)/2 {
			ans++
		}
	}
	return ans
}
