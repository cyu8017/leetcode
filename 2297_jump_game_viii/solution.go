// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

func minCost(nums []int, costs []int) int64 {
	n := len(nums)
	dp := make([]int64, n)
	for i := range dp {
		dp[i] = 1 << 60
	}
	dp[0] = 0
	stack1, stack2 := []int{}, []int{}
	for i := 0; i < n; i++ {
		for len(stack1) > 0 && nums[stack1[len(stack1)-1]] <= nums[i] {
			j := stack1[len(stack1)-1]
			stack1 = stack1[:len(stack1)-1]
			if dp[j]+int64(costs[i]) < dp[i] {
				dp[i] = dp[j] + int64(costs[i])
			}
		}
		for len(stack2) > 0 && nums[stack2[len(stack2)-1]] > nums[i] {
			j := stack2[len(stack2)-1]
			stack2 = stack2[:len(stack2)-1]
			if dp[j]+int64(costs[i]) < dp[i] {
				dp[i] = dp[j] + int64(costs[i])
			}
		}
		if len(stack1) > 0 {
			j := stack1[len(stack1)-1]
			if dp[j]+int64(costs[i]) < dp[i] {
				dp[i] = dp[j] + int64(costs[i])
			}
		}
		if len(stack2) > 0 {
			j := stack2[len(stack2)-1]
			if dp[j]+int64(costs[i]) < dp[i] {
				dp[i] = dp[j] + int64(costs[i])
			}
		}
		stack1 = append(stack1, i)
		stack2 = append(stack2, i)
	}
	return dp[n-1]
}
