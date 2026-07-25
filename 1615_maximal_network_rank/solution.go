// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

func maximalNetworkRank(n int, roads [][]int) int {
	degree := make([]int, n)
	edges := map[[2]int]bool{}
	for _, r := range roads {
		a, b := r[0], r[1]
		degree[a]++
		degree[b]++
		if a > b {
			a, b = b, a
		}
		edges[[2]int{a, b}] = true
	}
	ans := 0
	for a := 0; a < n; a++ {
		for b := a + 1; b < n; b++ {
			cur := degree[a] + degree[b]
			if edges[[2]int{a, b}] {
				cur--
			}
			if cur > ans {
				ans = cur
			}
		}
	}
	return ans
}
