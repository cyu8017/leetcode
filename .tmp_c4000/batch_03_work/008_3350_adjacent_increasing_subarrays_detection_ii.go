// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

func maxIncreasingSubarrays(nums []int) int {
	n := len(nums)
	up := make([]int, n)
	up[n-1] = 1
	for i := n - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			up[i] = up[i+1] + 1
		} else {
			up[i] = 1
		}
	}
	lo, hi := 1, n/2
	ok := func(k int) bool {
		for i := 0; i+2*k <= n; i++ {
			if up[i] >= k && up[i+k] >= k {
				return true
			}
		}
		return false
	}
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if ok(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
