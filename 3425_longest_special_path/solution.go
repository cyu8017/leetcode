// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

func longestSpecialPath(edges [][]int, nums []int) []int {
	n := len(nums)
	type edge struct{ to, w int }
	g := make([][]edge, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], edge{e[1], e[2]})
		g[e[1]] = append(g[e[1]], edge{e[0], e[2]})
	}
	bestLen, bestNodes := 0, 1
	last := map[int]int{}
	var dfs func(u, p, dist, left int, path []int)
	dfs = func(u, p, dist, left int, path []int) {
		prevPos, seen := last[nums[u]]
		last[nums[u]] = len(path)
		newLeft := left
		if seen && prevPos >= left {
			newLeft = prevPos + 1
		}
		path = append(path, dist)
		length := dist - path[newLeft]
		nodes := len(path) - newLeft
		if length > bestLen || (length == bestLen && nodes < bestNodes) {
			bestLen = length
			bestNodes = nodes
		}
		for _, e := range g[u] {
			if e.to == p {
				continue
			}
			dfs(e.to, u, dist+e.w, newLeft, path)
		}
		path = path[:len(path)-1]
		if seen {
			last[nums[u]] = prevPos
		} else {
			delete(last, nums[u])
		}
	}
	dfs(0, -1, 0, 0, []int{})
	return []int{bestLen, bestNodes}
}
