// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

func loudAndRich(richer [][]int, quiet []int) []int {
	n := len(quiet)
	graph := make([][]int, n)
	for _, e := range richer {
		a, b := e[0], e[1]
		graph[b] = append(graph[b], a)
	}
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	var dfs func(person int) int
	dfs = func(person int) int {
		if ans[person] != -1 {
			return ans[person]
		}
		best := person
		for _, richerPerson := range graph[person] {
			cand := dfs(richerPerson)
			if quiet[cand] < quiet[best] {
				best = cand
			}
		}
		ans[person] = best
		return best
	}
	for i := 0; i < n; i++ {
		dfs(i)
	}
	return ans
}
