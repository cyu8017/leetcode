// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

func treeDiameter(edges [][]int) int {
	if len(edges) == 0 {
		return 0
	}
	graph := map[int][]int{}
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}
	farthest := func(start int) (int, int) {
		type item struct{ node, dist int }
		q := []item{{start, 0}}
		seen := map[int]bool{start: true}
		last := item{start, 0}
		for len(q) > 0 {
			last = q[0]
			q = q[1:]
			for _, v := range graph[last.node] {
				if !seen[v] {
					seen[v] = true
					q = append(q, item{v, last.dist + 1})
				}
			}
		}
		return last.node, last.dist
	}
	endpoint, _ := farthest(edges[0][0])
	_, dist := farthest(endpoint)
	return dist
}
