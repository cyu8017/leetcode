// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

func longestArithSeqLength(nums []int) int {
	dp := make([]map[int]int, len(nums))
	ans := 1
	for j := 1; j < len(nums); j++ {
		dp[j] = map[int]int{}
		for i := 0; i < j; i++ {
			d := nums[j] - nums[i]
			prev := 1
			if dp[i] != nil {
				if v, ok := dp[i][d]; ok {
					prev = v
				}
			}
			dp[j][d] = prev + 1
			if dp[j][d] > ans {
				ans = dp[j][d]
			}
		}
	}
	return ans
}
