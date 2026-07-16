// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

func searchRange(nums []int, target int) []int {
	lowerBound := func() int {
		left, right := 0, len(nums)
		for left < right {
			mid := (left + right) / 2
			if nums[mid] < target {
				left = mid + 1
			} else {
				right = mid
			}
		}
		return left
	}

	upperBound := func() int {
		left, right := 0, len(nums)
		for left < right {
			mid := (left + right) / 2
			if nums[mid] <= target {
				left = mid + 1
			} else {
				right = mid
			}
		}
		return left
	}

	if len(nums) == 0 {
		return []int{-1, -1}
	}

	start := lowerBound()
	if start == len(nums) || nums[start] != target {
		return []int{-1, -1}
	}

	return []int{start, upperBound() - 1}
}
