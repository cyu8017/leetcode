// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

func findMaxAverage(nums []int, k int) float64 {
	window := 0
	for i := 0; i < k; i++ {
		window += nums[i]
	}
	best := window
	for i := k; i < len(nums); i++ {
		window += nums[i] - nums[i-k]
		if window > best {
			best = window
		}
	}
	return float64(best) / float64(k)
}
