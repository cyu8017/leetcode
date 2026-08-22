// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

func longestSpecialPath(edges [][]int, nums []int) []int {
	// allow at most one duplicate value
	n := len(nums)
	type edge struct{ to, w int }
	g := make([][]edge, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], edge{e[1], e[2]})
		g[e[1]] = append(g[e[1]], edge{e[0], e[2]})
	}
	bestLen, bestNodes := 0, 1
	var dfs func(u, p, dist int, pathVals []int, pathDist []int, dup int)
	dfs = func(u, p, dist int, pathVals []int, pathDist []int, dup int) {
		pathVals = append(pathVals, nums[u])
		pathDist = append(pathDist, dist)
		// find leftmost valid start
		freq := map[int]int{}
		dups := 0
		left := 0
		for right := 0; right < len(pathVals); right++ {
			freq[pathVals[right]]++
			if freq[pathVals[right]] == 2 {
				dups++
			}
			for dups > 1 {
				if freq[pathVals[left]] == 2 {
					dups--
				}
				freq[pathVals[left]]--
				left++
			}
		}
		length := dist - pathDist[left]
		nodes := len(pathVals) - left
		if length > bestLen || (length == bestLen && nodes < bestNodes) {
			bestLen = length
			bestNodes = nodes
		}
		for _, e := range g[u] {
			if e.to == p {
				continue
			}
			dfs(e.to, u, dist+e.w, pathVals, pathDist, dup)
		}
	}
	dfs(0, -1, 0, nil, nil, 0)
	return []int{bestLen, bestNodes}
}
