// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

func knightProbability(n int, k int, row int, column int) float64 {
	moves := [][2]int{{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}}
	dp := make([][]float64, n)
	for i := range dp {
		dp[i] = make([]float64, n)
	}
	dp[row][column] = 1.0
	for step := 0; step < k; step++ {
		nxt := make([][]float64, n)
		for i := range nxt {
			nxt[i] = make([]float64, n)
		}
		for r := 0; r < n; r++ {
			for c := 0; c < n; c++ {
				if dp[r][c] == 0 {
					continue
				}
				for _, d := range moves {
					nr, nc := r+d[0], c+d[1]
					if nr >= 0 && nr < n && nc >= 0 && nc < n {
						nxt[nr][nc] += dp[r][c] / 8.0
					}
				}
			}
		}
		dp = nxt
	}
	total := 0.0
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			total += dp[r][c]
		}
	}
	return total
}
