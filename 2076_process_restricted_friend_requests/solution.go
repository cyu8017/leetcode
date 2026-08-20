// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

func friendRequests(n int, restrictions [][]int, requests [][]int) []bool {
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	union := func(a, b int) {
		ra, rb := find(a), find(b)
		if ra != rb {
			parent[ra] = rb
		}
	}
	ans := make([]bool, len(requests))
	for i, req := range requests {
		u, v := find(req[0]), find(req[1])
		ok := true
		if u != v {
			for _, r := range restrictions {
				x, y := find(r[0]), find(r[1])
				if (x == u && y == v) || (x == v && y == u) {
					ok = false
					break
				}
			}
		}
		ans[i] = ok
		if ok {
			union(u, v)
		}
	}
	return ans
}
