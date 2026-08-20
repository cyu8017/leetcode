// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

func shortestPathLength(graph [][]int) int {
	n := len(graph)
	target := (1 << n) - 1
	type item struct{ node, mask, dist int }
	queue := []item{}
	seen := map[[2]int]bool{}
	for i := 0; i < n; i++ {
		queue = append(queue, item{i, 1 << i, 0})
		seen[[2]int{i, 1 << i}] = true
	}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.mask == target {
			return cur.dist
		}
		for _, nxt := range graph[cur.node] {
			nmask := cur.mask | (1 << nxt)
			state := [2]int{nxt, nmask}
			if !seen[state] {
				seen[state] = true
				queue = append(queue, item{nxt, nmask, cur.dist + 1})
			}
		}
	}
	return -1
}
