// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

func minMaxWeight(n int, edges [][]int, threshold int) int {
	ok := func(mid int) bool {
		g := make([][]int, n)
		for _, e := range edges {
			a, b, w := e[0], e[1], e[2]
			if w <= mid {
				// reverse: we need reach 0, so edge a->b means from b can go to a in reverse
				g[b] = append(g[b], a)
			}
		}
		vis := make([]bool, n)
		q := []int{0}
		vis[0] = true
		cnt := 1
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			for _, v := range g[u] {
				if !vis[v] {
					vis[v] = true
					cnt++
					q = append(q, v)
				}
			}
		}
		return cnt == n
	}
	lo, hi := 1, 1000001
	ans := -1
	for lo < hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			ans = mid
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	_ = threshold
	return ans
}
