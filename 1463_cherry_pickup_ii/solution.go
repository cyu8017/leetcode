// LeetCode 1463 - Cherry Pickup II
// https://leetcode.com/problems/cherry-pickup-ii/

func cherryPickup(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	type key struct{ a, b int }
	dp := map[key]int{{0, n - 1}: grid[0][0]}
	if n > 1 {
		dp[key{0, n - 1}] += grid[0][n-1]
	}
	for r := 1; r < m; r++ {
		nxt := map[key]int{}
		for kb, score := range dp {
			a, b := kb.a, kb.b
			for _, da := range []int{-1, 0, 1} {
				for _, db := range []int{-1, 0, 1} {
					na, nb := a+da, b+db
					if na >= 0 && na < n && nb >= 0 && nb < n {
						val := score + grid[r][na]
						if na != nb {
							val += grid[r][nb]
						}
						k := key{na, nb}
						if v, ok := nxt[k]; !ok || val > v {
							nxt[k] = val
						}
					}
				}
			}
		}
		dp = nxt
	}
	ans := 0
	for _, v := range dp {
		if v > ans {
			ans = v
		}
	}
	return ans
}
