// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

func minCost(n int, cost [][]int) int64 {
	const inf = int64(1 << 60)
	// pair houses i and n-1-i
	m := n / 2
	dp := [3][3]int64{}
	for a := 0; a < 3; a++ {
		for b := 0; b < 3; b++ {
			if a == b {
				dp[a][b] = inf
			} else {
				dp[a][b] = int64(cost[0][a] + cost[n-1][b])
			}
		}
	}
	for i := 1; i < m; i++ {
		ndp := [3][3]int64{}
		for a := 0; a < 3; a++ {
			for b := 0; b < 3; b++ {
				ndp[a][b] = inf
			}
		}
		for pa := 0; pa < 3; pa++ {
			for pb := 0; pb < 3; pb++ {
				if dp[pa][pb] >= inf {
					continue
				}
				for a := 0; a < 3; a++ {
					if a == pa {
						continue
					}
					for b := 0; b < 3; b++ {
						if b == pb || a == b {
							continue
						}
						v := dp[pa][pb] + int64(cost[i][a]+cost[n-1-i][b])
						if v < ndp[a][b] {
							ndp[a][b] = v
						}
					}
				}
			}
		}
		dp = ndp
	}
	ans := inf
	for a := 0; a < 3; a++ {
		for b := 0; b < 3; b++ {
			if dp[a][b] < ans {
				ans = dp[a][b]
			}
		}
	}
	return ans
}
