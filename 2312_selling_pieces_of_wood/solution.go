// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

func sellingWood(m int, n int, prices [][]int) int64 {
	price := make([][]int64, m+1)
	dp := make([][]int64, m+1)
	for i := 0; i <= m; i++ {
		price[i] = make([]int64, n+1)
		dp[i] = make([]int64, n+1)
	}
	for _, p := range prices {
		price[p[0]][p[1]] = int64(p[2])
	}
	for h := 1; h <= m; h++ {
		for w := 1; w <= n; w++ {
			best := price[h][w]
			for i := 1; i < h; i++ {
				if dp[i][w]+dp[h-i][w] > best {
					best = dp[i][w] + dp[h-i][w]
				}
			}
			for j := 1; j < w; j++ {
				if dp[h][j]+dp[h][w-j] > best {
					best = dp[h][j] + dp[h][w-j]
				}
			}
			dp[h][w] = best
		}
	}
	return dp[m][n]
}
