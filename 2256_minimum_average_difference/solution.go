// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

func minimumAverageDifference(nums []int) int {
	n := len(nums)
	var total int64
	for _, v := range nums {
		total += int64(v)
	}
	var left int64
	bestDiff := int64(1 << 62)
	bestIdx := 0
	for i := 0; i < n; i++ {
		left += int64(nums[i])
		leftAvg := left / int64(i+1)
		var rightAvg int64
		if i != n-1 {
			rightAvg = (total - left) / int64(n-i-1)
		}
		diff := leftAvg - rightAvg
		if diff < 0 {
			diff = -diff
		}
		if diff < bestDiff {
			bestDiff = diff
			bestIdx = i
		}
	}
	return bestIdx
}
