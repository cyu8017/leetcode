// LeetCode 3420 - Count Non Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

func countNonDecreasingSubarrays(nums []int, k int) int64 {
	n := len(nums)
	var ans int64
	for i := 0; i < n; i++ {
		cost := 0
		maxV := nums[i]
		for j := i; j < n; j++ {
			if nums[j] >= maxV {
				maxV = nums[j]
			} else {
				cost += maxV - nums[j]
			}
			if cost > k {
				break
			}
			ans++
		}
	}
	return ans
}
