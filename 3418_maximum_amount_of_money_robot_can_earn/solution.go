// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

func maximumAmount(coins [][]int) int {
	m, n := len(coins), len(coins[0])
	const neg = -1 << 30
	dp := make([][][3]int, m)
	for i := range dp {
		dp[i] = make([][3]int, n)
		for j := range dp[i] {
			dp[i][j] = [3]int{neg, neg, neg}
		}
	}
	// neutralize 0,1,2 robberies
	for k := 0; k < 3; k++ {
		if coins[0][0] >= 0 {
			dp[0][0][k] = coins[0][0]
		} else if k > 0 {
			dp[0][0][k] = 0 // neutralize
			if k >= 1 {
				dp[0][0][0] = coins[0][0] // also option take
			}
		} else {
			dp[0][0][0] = coins[0][0]
		}
	}
	if coins[0][0] < 0 {
		dp[0][0][0] = coins[0][0]
		dp[0][0][1] = 0
		dp[0][0][2] = 0
	} else {
		dp[0][0][0] = coins[0][0]
		dp[0][0][1] = coins[0][0]
		dp[0][0][2] = coins[0][0]
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			for k := 0; k < 3; k++ {
				best := neg
				if i > 0 {
					best = max3418(best, dp[i-1][j][k])
				}
				if j > 0 {
					best = max3418(best, dp[i][j-1][k])
				}
				if best == neg {
					continue
				}
				if coins[i][j] >= 0 {
					dp[i][j][k] = best + coins[i][j]
				} else {
					// take
					dp[i][j][k] = max3418(dp[i][j][k], best+coins[i][j])
					// neutralize if k>0 from k-1
				}
			}
			for k := 1; k < 3; k++ {
				best := neg
				if i > 0 {
					best = max3418(best, dp[i-1][j][k-1])
				}
				if j > 0 {
					best = max3418(best, dp[i][j-1][k-1])
				}
				if best != neg && coins[i][j] < 0 {
					dp[i][j][k] = max3418(dp[i][j][k], best)
				}
			}
		}
	}
	return max3418(dp[m-1][n-1][0], max3418(dp[m-1][n-1][1], dp[m-1][n-1][2]))
}

func max3418(a, b int) int {
	if a > b {
		return a
	}
	return b
}
