// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

func gardenNoAdj(n int, paths [][]int) []int {
	graph := make([][]int, n+1)
	for _, p := range paths {
		a, b := p[0], p[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	ans := make([]int, n+1)
	for garden := 1; garden <= n; garden++ {
		used := [5]bool{}
		for _, nei := range graph[garden] {
			used[ans[nei]] = true
		}
		for c := 1; c <= 4; c++ {
			if !used[c] {
				ans[garden] = c
				break
			}
		}
	}
	return ans[1:]
}
