// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

func minimumFuelCost(roads [][]int, seats int) int64 {
	n := len(roads) + 1
	g := make([][]int, n)
	for _, r := range roads {
		g[r[0]] = append(g[r[0]], r[1])
		g[r[1]] = append(g[r[1]], r[0])
	}
	var ans int64
	var dfs func(u, p int) int
	dfs = func(u, p int) int {
		people := 1
		for _, v := range g[u] {
			if v != p {
				people += dfs(v, u)
			}
		}
		if u != 0 {
			ans += int64((people + seats - 1) / seats)
		}
		return people
	}
	dfs(0, -1)
	return ans
}
