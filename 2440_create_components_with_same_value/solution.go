// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

func componentValue(nums []int, edges [][]int) int {
	n := len(nums)
	total := 0
	for _, x := range nums {
		total += x
	}
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	var dfs func(u, p, target int) int
	dfs = func(u, p, target int) int {
		sum := nums[u]
		for _, v := range g[u] {
			if v == p {
				continue
			}
			sub := dfs(v, u, target)
			if sub < 0 {
				return -1
			}
			sum += sub
		}
		if sum > target {
			return -1
		}
		if sum == target {
			return 0
		}
		return sum
	}
	for parts := n; parts >= 1; parts-- {
		if total%parts != 0 {
			continue
		}
		target := total / parts
		if dfs(0, -1, target) == 0 {
			return parts - 1
		}
	}
	return 0
}
