// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

func minOperationsToMakeMedianK(nums []int, k int) (ans int64) {
	sort.Ints(nums)
	n := len(nums)
	m := n >> 1
	ans = int64(abs(nums[m] - k))
	if nums[m] > k {
		for i := m - 1; i >= 0 && nums[i] > k; i-- {
			ans += int64(nums[i] - k)
		}
	} else {
		for i := m + 1; i < n && nums[i] < k; i++ {
			ans += int64(k - nums[i])
		}
	}
	return
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
