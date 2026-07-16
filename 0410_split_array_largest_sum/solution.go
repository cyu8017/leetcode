// LeetCode 0410 - Split Array Largest Sum
// https://leetcode.com/problems/split-array-largest-sum/

func splitArray(nums []int, k int) int {
	left := nums[0]
	right := 0
	for _, value := range nums {
		if value > left {
			left = value
		}
		right += value
	}

	canSplit := func(limit int) bool {
		parts := 1
		current := 0
		for _, value := range nums {
			if current+value > limit {
				parts++
				current = 0
			}
			current += value
		}
		return parts <= k
	}

	for left < right {
		mid := left + (right-left)/2
		if canSplit(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}
