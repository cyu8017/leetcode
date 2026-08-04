// LeetCode 1444 - Number of Ways of Cutting a Pizza
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

func ways(pizza []string, k int) int {
	const mod = 1000000007
	rows, cols := len(pizza), len(pizza[0])
	apples := make([][]int, rows+1)
	for i := range apples {
		apples[i] = make([]int, cols+1)
	}
	for r := rows - 1; r >= 0; r-- {
		for c := cols - 1; c >= 0; c-- {
			add := 0
			if pizza[r][c] == 'A' {
				add = 1
			}
			apples[r][c] = add + apples[r+1][c] + apples[r][c+1] - apples[r+1][c+1]
		}
	}
	dp := make([][]int, rows)
	for r := range dp {
		dp[r] = make([]int, cols)
		for c := range dp[r] {
			if apples[r][c] > 0 {
				dp[r][c] = 1
			}
		}
	}
	for cut := 1; cut < k; cut++ {
		nxt := make([][]int, rows)
		for r := range nxt {
			nxt[r] = make([]int, cols)
		}
		for r := 0; r < rows; r++ {
			for c := 0; c < cols; c++ {
				for nr := r + 1; nr < rows; nr++ {
					if apples[r][c] > apples[nr][c] {
						nxt[r][c] += dp[nr][c]
					}
				}
				for nc := c + 1; nc < cols; nc++ {
					if apples[r][c] > apples[r][nc] {
						nxt[r][c] += dp[r][nc]
					}
				}
				nxt[r][c] %= mod
			}
		}
		dp = nxt
	}
	return dp[0][0]
}
