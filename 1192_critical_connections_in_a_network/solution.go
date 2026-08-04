// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

func criticalConnections(n int, connections [][]int) [][]int {
	graph := make([][]int, n)
	for _, e := range connections {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}
	disc := make([]int, n)
	low := make([]int, n)
	for i := range disc {
		disc[i] = -1
	}
	time := 0
	bridges := [][]int{}
	var dfs func(int, int)
	dfs = func(node, parent int) {
		disc[node] = time
		low[node] = time
		time++
		for _, nxt := range graph[node] {
			if nxt == parent {
				continue
			}
			if disc[nxt] == -1 {
				dfs(nxt, node)
				if low[nxt] < low[node] {
					low[node] = low[nxt]
				}
				if low[nxt] > disc[node] {
					a, b := node, nxt
					if a > b {
						a, b = b, a
					}
					bridges = append(bridges, []int{a, b})
				}
			} else if disc[nxt] < low[node] {
				low[node] = disc[nxt]
			}
		}
	}
	dfs(0, -1)
	return bridges
}
