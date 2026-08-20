// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

func maximumDifference(nums []int) int {
	ans := -1
	mn := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > mn {
			if nums[i]-mn > ans {
				ans = nums[i] - mn
			}
		} else {
			mn = nums[i]
		}
	}
	return ans
}
