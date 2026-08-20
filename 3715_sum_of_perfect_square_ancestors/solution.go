// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

func sumOfAncestors(n int, edges [][]int, nums []int) int64 {
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	// square-free kernel of number
	kernel := func(x int) int {
		res := 1
		for p := 2; p*p <= x; p++ {
			cnt := 0
			for x%p == 0 {
				x /= p
				cnt++
			}
			if cnt%2 == 1 {
				res *= p
			}
		}
		if x > 1 {
			res *= x
		}
		return res
	}
	ks := make([]int, n)
	for i, v := range nums {
		ks[i] = kernel(v)
	}
	freq := map[int]int{}
	var ans int64
	var dfs func(u, p int)
	dfs = func(u, p int) {
		ans += int64(freq[ks[u]])
		freq[ks[u]]++
		for _, v := range graph[u] {
			if v != p {
				dfs(v, u)
			}
		}
		freq[ks[u]]--
	}
	dfs(0, -1)
	return ans
}
