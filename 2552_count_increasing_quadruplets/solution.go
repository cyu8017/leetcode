// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/


func countQuadruplets(nums []int) int64 {
	n := len(nums)
	var ans int64
	great := make([]int, n)
	for j := 0; j < n; j++ {
		less := 0
		for i := 0; i < j; i++ {
			if nums[i] < nums[j] {
				ans += int64(great[i])
				less++
			} else if nums[i] > nums[j] {
				great[i]++
			}
		}
		_ = less
	}
	return ans
}
