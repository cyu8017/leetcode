// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

func maxScore(edges [][]int) int64 {
	n := len(edges) + 1
	type edge struct{ to, w int }
	g := make([][]edge, n)
	for i := 1; i < n; i++ {
		p, w := edges[i-1][0], edges[i-1][1]
		g[p] = append(g[p], edge{i, w})
		g[i] = append(g[i], edge{p, w})
	}
	var dfs func(u, p int) (int64, int64) // with parent edge unused, with parent edge used somehow
	// return: (best if edge to parent not taken, best if we can take edge to parent)
	dfs = func(u, p int) (int64, int64) {
		var base int64
		bestGain := int64(0)
		for _, e := range g[u] {
			if e.to == p {
				continue
			}
			without, with := dfs(e.to, u)
			base += without
			gain := with + int64(e.w) - without
			if gain > bestGain {
				bestGain = gain
			}
		}
		return base + bestGain, base
	}
	ans, _ := dfs(0, -1)
	return ans
}
