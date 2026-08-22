// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

func subtreeInversionSum(edges [][]int, nums []int, k int) int64 {
	n := len(edges) + 1
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -1
	}
	type key struct {
		u, steps int
		inv      bool
	}
	memo := map[key]int64{}
	var dp func(u, steps int, inv bool) int64
	dp = func(u, steps int, inv bool) int64 {
		kk := key{u, steps, inv}
		if v, ok := memo[kk]; ok {
			return v
		}
		num := int64(nums[u])
		if inv {
			num = -num
		}
		negNum := -num
		for _, v := range graph[u] {
			if v == parent[u] {
				continue
			}
			parent[v] = u
			ns := steps + 1
			if ns > k {
				ns = k
			}
			num += dp(v, ns, inv)
			if steps == k {
				negNum += dp(v, 1, !inv)
			}
		}
		res := num
		if steps == k && negNum > res {
			res = negNum
		}
		memo[kk] = res
		return res
	}
	return dp(0, k, false)
}
