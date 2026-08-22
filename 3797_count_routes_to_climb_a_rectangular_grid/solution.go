// LeetCode 3797 - Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

func countRoutes(grid []string, d int) int {
	const mod = 1000000007
	n, m := len(grid), len(grid[0])
	upRadius := 0
	for (upRadius+1)*(upRadius+1)+1 <= d*d {
		upRadius++
	}
	arrived := make([]int, m)
	for c := 0; c < m; c++ {
		if grid[n-1][c] == '.' {
			arrived[c] = 1
		}
	}
	rowWays := func(row int, base []int) ([]int, []int) {
		pref := make([]int, m+1)
		for i, x := range base {
			pref[i+1] = (pref[i] + x) % mod
		}
		horizontal := make([]int, m)
		for c := 0; c < m; c++ {
			if grid[row][c] == '#' {
				continue
			}
			l, r := c-d, c+d
			if l < 0 {
				l = 0
			}
			if r >= m {
				r = m - 1
			}
			horizontal[c] = (pref[r+1] - pref[l] - base[c]) % mod
			if horizontal[c] < 0 {
				horizontal[c] += mod
			}
		}
		return base, horizontal
	}
	for r := n - 1; r >= 0; r-- {
		base, horizontal := rowWays(r, arrived)
		if r == 0 {
			ans := 0
			for c := 0; c < m; c++ {
				ans = (ans + base[c] + horizontal[c]) % mod
			}
			return ans
		}
		pref := make([]int, m+1)
		for c := 0; c < m; c++ {
			pref[c+1] = (pref[c] + base[c] + horizontal[c]) % mod
		}
		next := make([]int, m)
		for c := 0; c < m; c++ {
			if grid[r-1][c] == '#' {
				continue
			}
			l, rr := c-upRadius, c+upRadius
			if l < 0 {
				l = 0
			}
			if rr >= m {
				rr = m - 1
			}
			next[c] = pref[rr+1] - pref[l]
			if next[c] < 0 {
				next[c] += mod
			}
		}
		arrived = next
	}
	return 0
}