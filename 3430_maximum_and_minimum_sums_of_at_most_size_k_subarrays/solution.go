// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

func minMaxSubarraySum(nums []int, k int) int64 {
	n := len(nums)
	var ans int64
	for i := 0; i < n; i++ {
		mn, mx := nums[i], nums[i]
		for j := i; j < n && j-i+1 <= k; j++ {
			if nums[j] < mn {
				mn = nums[j]
			}
			if nums[j] > mx {
				mx = nums[j]
			}
			ans += int64(mn + mx)
		}
	}
	return ans
}
