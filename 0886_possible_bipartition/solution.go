// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

func possibleBipartition(n int, dislikes [][]int) bool {
	graph := make([][]int, n+1)
	for _, e := range dislikes {
		a, b := e[0], e[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	color := map[int]int{}
	for start := 1; start <= n; start++ {
		if _, ok := color[start]; ok {
			continue
		}
		queue := []int{start}
		color[start] = 0
		for len(queue) > 0 {
			node := queue[0]
			queue = queue[1:]
			for _, nei := range graph[node] {
				if _, ok := color[nei]; !ok {
					color[nei] = color[node] ^ 1
					queue = append(queue, nei)
				} else if color[nei] == color[node] {
					return false
				}
			}
		}
	}
	return true
}
