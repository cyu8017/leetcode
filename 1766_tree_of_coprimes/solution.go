// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

func getCoprimes(nums []int, edges [][]int) []int {
	n := len(nums)
	adj := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	path := make([][][2]int, 51)
	var dfs func(node, parent, depth int)
	dfs = func(node, parent, depth int) {
		bestDepth, bestNode := -1, -1
		val := nums[node]
		for d := 1; d <= 50; d++ {
			if gcd(val, d) == 1 && len(path[d]) > 0 {
				cand := path[d][len(path[d])-1]
				if cand[0] > bestDepth {
					bestDepth = cand[0]
					bestNode = cand[1]
				}
			}
		}
		ans[node] = bestNode
		path[val] = append(path[val], [2]int{depth, node})
		for _, nxt := range adj[node] {
			if nxt != parent {
				dfs(nxt, node, depth+1)
			}
		}
		path[val] = path[val][:len(path[val])-1]
	}
	dfs(0, -1, 0)
	return ans
}
