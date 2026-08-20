// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

func findMaxAverage(nums []int, k int) float64 {
	canReach := func(mid float64) bool {
		prefix := 0.0
		for i := 0; i < k; i++ {
			prefix += float64(nums[i]) - mid
		}
		if prefix >= 0 {
			return true
		}
		prev, minPrev := 0.0, 0.0
		for i := k; i < len(nums); i++ {
			prefix += float64(nums[i]) - mid
			prev += float64(nums[i-k]) - mid
			if prev < minPrev {
				minPrev = prev
			}
			if prefix-minPrev >= 0 {
				return true
			}
		}
		return false
	}
	left, right := float64(nums[0]), float64(nums[0])
	for _, num := range nums {
		if float64(num) < left {
			left = float64(num)
		}
		if float64(num) > right {
			right = float64(num)
		}
	}
	for i := 0; i < 80; i++ {
		mid := (left + right) / 2
		if canReach(mid) {
			left = mid
		} else {
			right = mid
		}
	}
	return left
}
