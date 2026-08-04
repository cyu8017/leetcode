// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

func canBeIncreasing(nums []int) bool {
	check := func(skip int) bool {
		prev := -1
		hasPrev := false
		for i, x := range nums {
			if i == skip {
				continue
			}
			if hasPrev && x <= prev {
				return false
			}
			prev = x
			hasPrev = true
		}
		return true
	}
	for i := 1; i < len(nums); i++ {
		if nums[i] <= nums[i-1] {
			return check(i-1) || check(i)
		}
	}
	return true
}
