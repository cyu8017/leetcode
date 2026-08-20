// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/


func maxMoves(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dp := make([]int, m)
	for c := n - 2; c >= 0; c-- {
		ndp := make([]int, m)
		for r := 0; r < m; r++ {
			best := 0
			for dr := -1; dr <= 1; dr++ {
				nr := r + dr
				if nr >= 0 && nr < m && grid[nr][c+1] > grid[r][c] {
					cand := 1 + dp[nr]
					if cand > best {
						best = cand
					}
				}
			}
			ndp[r] = best
		}
		dp = ndp
	}
	ans := 0
	for _, v := range dp {
		if v > ans {
			ans = v
		}
	}
	return ans
}
