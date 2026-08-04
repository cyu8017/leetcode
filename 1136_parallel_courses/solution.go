// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

func minimumSemesters(n int, relations [][]int) int {
	graph := make([][]int, n+1)
	indeg := make([]int, n+1)
	for _, r := range relations {
		graph[r[0]] = append(graph[r[0]], r[1])
		indeg[r[1]]++
	}
	queue := []int{}
	for i := 1; i <= n; i++ {
		if indeg[i] == 0 {
			queue = append(queue, i)
		}
	}
	semesters, taken := 0, 0
	for len(queue) > 0 {
		size := len(queue)
		semesters++
		for i := 0; i < size; i++ {
			u := queue[0]
			queue = queue[1:]
			taken++
			for _, v := range graph[u] {
				indeg[v]--
				if indeg[v] == 0 {
					queue = append(queue, v)
				}
			}
		}
	}
	if taken == n {
		return semesters
	}
	return -1
}
