// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

func findIndices(nums []int, indexDifference int, valueDifference int) []int {
	n := len(nums)
	minIdx, maxIdx := 0, 0
	for j := indexDifference; j < n; j++ {
		i := j - indexDifference
		if nums[i] < nums[minIdx] {
			minIdx = i
		}
		if nums[i] > nums[maxIdx] {
			maxIdx = i
		}
		if nums[j]-nums[minIdx] >= valueDifference {
			return []int{minIdx, j}
		}
		if nums[maxIdx]-nums[j] >= valueDifference {
			return []int{maxIdx, j}
		}
	}
	return []int{-1, -1}
}
