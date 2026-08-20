// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

func countSubarrays(nums []int) int64 {
	var ans, len_ int64
	for i := 0; i < len(nums); i++ {
		if i > 0 && nums[i] > nums[i-1] {
			len_++
		} else {
			len_ = 1
		}
		ans += len_
	}
	return ans
}
