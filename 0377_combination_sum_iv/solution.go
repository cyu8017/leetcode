// LeetCode 0377 - Combination Sum IV
// https://leetcode.com/problems/combination-sum-iv/

func combinationSum4(nums []int, target int) int {
	dp := make([]int, target+1)
	dp[0] = 1

	for amount := 1; amount <= target; amount++ {
		for _, num := range nums {
			if amount >= num {
				dp[amount] += dp[amount-num]
			}
		}
	}

	return dp[target]
}
