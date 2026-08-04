// LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

func minReorder(n int, connections [][]int) int {
	type edge struct{ nei, cost int }
	graph := make([][]edge, n)
	for _, c := range connections {
		a, b := c[0], c[1]
		graph[a] = append(graph[a], edge{b, 1})
		graph[b] = append(graph[b], edge{a, 0})
	}
	ans := 0
	stack := []int{0}
	seen := map[int]bool{0: true}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, e := range graph[node] {
			if !seen[e.nei] {
				seen[e.nei] = true
				stack = append(stack, e.nei)
				ans += e.cost
			}
		}
	}
	return ans
}
