// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

func numRollsToTarget(n int, k int, target int) int {
	const MOD = 1000000007
	dp := make([]int, target+1)
	dp[0] = 1
	for roll := 0; roll < n; roll++ {
		newDP := make([]int, target+1)
		for s := 0; s <= target; s++ {
			if dp[s] == 0 {
				continue
			}
			for face := 1; face <= k; face++ {
				if s+face <= target {
					newDP[s+face] = (newDP[s+face] + dp[s]) % MOD
				}
			}
		}
		dp = newDP
	}
	return dp[target]
}
