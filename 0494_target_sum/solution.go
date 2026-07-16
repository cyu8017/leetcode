// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

func findTargetSumWays(nums []int, target int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	if (total+target)%2 != 0 || abs(target) > total {
		return 0
	}
	need := (total + target) / 2
	dp := make([]int, need+1)
	dp[0] = 1
	for _, num := range nums {
		for amount := need; amount >= num; amount-- {
			dp[amount] += dp[amount-num]
		}
	}
	return dp[need]
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
