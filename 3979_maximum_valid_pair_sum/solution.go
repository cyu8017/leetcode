// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

func maxValidPairSum(nums []int, k int) int {
	var ans, x int
	for j := k; j < len(nums); j++ {
		y := nums[j]
		x = max(x, nums[j-k])
		ans = max(ans, x+y)
	}
	return ans
}
