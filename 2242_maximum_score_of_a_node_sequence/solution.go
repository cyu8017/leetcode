// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

func maximumScore(scores []int, edges [][]int) int {
	n := len(scores)
	top := make([][]int, n)
	g := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		g[a] = append(g[a], b)
		g[b] = append(g[b], a)
	}
	for i := 0; i < n; i++ {
		sortNeighbors := append([]int{}, g[i]...)
		// keep top 3 by score
		for _, v := range sortNeighbors {
			top[i] = append(top[i], v)
			// insertion keep desc score
			for j := len(top[i]) - 1; j > 0; j-- {
				if scores[top[i][j]] > scores[top[i][j-1]] {
					top[i][j], top[i][j-1] = top[i][j-1], top[i][j]
				}
			}
			if len(top[i]) > 3 {
				top[i] = top[i][:3]
			}
		}
	}
	ans := -1
	for _, e := range edges {
		a, b := e[0], e[1]
		for _, c := range top[a] {
			if c == b {
				continue
			}
			for _, d := range top[b] {
				if d == a || d == c {
					continue
				}
				sum := scores[a] + scores[b] + scores[c] + scores[d]
				if sum > ans {
					ans = sum
				}
			}
		}
	}
	return ans
}
