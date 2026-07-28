// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

func missingElement(nums []int, k int) int {
	missing := func(i int) int {
		return nums[i] - nums[0] - i
	}
	n := len(nums)
	if k > missing(n-1) {
		return nums[n-1] + k - missing(n-1)
	}
	lo, hi := 0, n-1
	for lo < hi {
		mid := (lo + hi) / 2
		if missing(mid) < k {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return nums[lo-1] + k - missing(lo-1)
}
