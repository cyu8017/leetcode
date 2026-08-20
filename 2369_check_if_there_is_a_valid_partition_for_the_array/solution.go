// LeetCode 2369 - Check if There is a Valid Partition For The Array
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

func validPartition(nums []int) bool {
	n := len(nums)
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 1; i <= n; i++ {
		if i >= 2 && nums[i-1] == nums[i-2] && dp[i-2] {
			dp[i] = true
		}
		if i >= 3 && nums[i-1] == nums[i-2] && nums[i-2] == nums[i-3] && dp[i-3] {
			dp[i] = true
		}
		if i >= 3 && nums[i-1] == nums[i-2]+1 && nums[i-2] == nums[i-3]+1 && dp[i-3] {
			dp[i] = true
		}
	}
	return dp[n]
}
