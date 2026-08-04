// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

func shortestAlternatingPaths(n int, redEdges [][]int, blueEdges [][]int) []int {
	graph := [2][][]int{make([][]int, n), make([][]int, n)}
	for _, e := range redEdges {
		graph[0][e[0]] = append(graph[0][e[0]], e[1])
	}
	for _, e := range blueEdges {
		graph[1][e[0]] = append(graph[1][e[0]], e[1])
	}
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	type state struct{ node, color, dist int }
	queue := []state{{0, 0, 0}, {0, 1, 0}}
	seen := [2][]bool{make([]bool, n), make([]bool, n)}
	seen[0][0], seen[1][0] = true, true
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if ans[cur.node] == -1 {
			ans[cur.node] = cur.dist
		}
		nextColor := 1 - cur.color
		for _, nxt := range graph[cur.color][cur.node] {
			if !seen[nextColor][nxt] {
				seen[nextColor][nxt] = true
				queue = append(queue, state{nxt, nextColor, cur.dist + 1})
			}
		}
	}
	return ans
}
