// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

func findIndices(nums []int, indexDifference int, valueDifference int) []int {
	n := len(nums)
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			di := j - i
			if di < 0 {
				di = -di
			}
			dv := nums[i] - nums[j]
			if dv < 0 {
				dv = -dv
			}
			if di >= indexDifference && dv >= valueDifference {
				return []int{i, j}
			}
		}
	}
	return []int{-1, -1}
}
