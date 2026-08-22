// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

func absDifference(nums []int, k int) (ans int) {
	slices.Sort(nums)
	for i := 0; i < k; i++ {
		ans += nums[len(nums)-i-1] - nums[i]
	}
	return
}
