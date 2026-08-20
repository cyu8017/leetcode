// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

func hasIncreasingSubarrays(nums []int, k int) bool {
	n := len(nums)
	inc := func(start int) bool {
		for i := start; i+1 < start+k; i++ {
			if nums[i] >= nums[i+1] {
				return false
			}
		}
		return true
	}
	for i := 0; i+2*k <= n; i++ {
		if inc(i) && inc(i+k) {
			return true
		}
	}
	return false
}
