// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

func maxLen(n int, edges [][]int, label string) int {
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	ans := 1
	for i := 0; i < n; i++ {
		ans = max(ans, expandPal(g, label, i, i))
		for _, j := range g[i] {
			if i < j && label[i] == label[j] {
				ans = max(ans, expandPal(g, label, i, j))
			}
		}
	}
	return ans
}

func expandPal(g [][]int, label string, l, r int) int {
	type pair struct{ a, b int }
	vis := map[pair]bool{}
	type state struct{ l, r, length int }
	q := []state{{l, r, 1}}
	if l != r {
		q[0].length = 2
	}
	best := q[0].length
	vis[pair{min(l, r), max(l, r)}] = true
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, a := range g[cur.l] {
			for _, b := range g[cur.r] {
				if a == b || label[a] != label[b] {
					continue
				}
				p := pair{min(a, b), max(a, b)}
				if vis[p] {
					continue
				}
				vis[p] = true
				nl := cur.length + 2
				if nl > best {
					best = nl
				}
				q = append(q, state{a, b, nl})
			}
		}
	}
	return best
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
