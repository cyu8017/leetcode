// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

func predictTheWinner(nums []int) bool {
	n := len(nums)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
		dp[i][i] = nums[i]
	}
	for length := 2; length <= n; length++ {
		for left := 0; left+length-1 < n; left++ {
			right := left + length - 1
			leftScore := nums[left] - dp[left+1][right]
			rightScore := nums[right] - dp[left][right-1]
			if leftScore > rightScore {
				dp[left][right] = leftScore
			} else {
				dp[left][right] = rightScore
			}
		}
	}
	return dp[0][n-1] >= 0
}
