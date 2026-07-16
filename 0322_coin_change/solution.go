// LeetCode 0322 - Coin Change
// https://leetcode.com/problems/coin-change/

func coinChange(coins []int, amount int) int {
	maxValue := amount + 1
	dp := make([]int, amount+1)
	for value := range dp {
		dp[value] = maxValue
	}
	dp[0] = 0
	for _, coin := range coins {
		for value := coin; value <= amount; value++ {
			if dp[value-coin]+1 < dp[value] {
				dp[value] = dp[value-coin] + 1
			}
		}
	}
	if dp[amount] == maxValue {
		return -1
	}
	return dp[amount]
}
