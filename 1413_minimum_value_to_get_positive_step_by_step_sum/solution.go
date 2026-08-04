// LeetCode 1413 - Minimum Value to Get Positive Step by Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

func minStartValue(nums []int) int {
	prefix, lowest := 0, 0
	for _, value := range nums {
		prefix += value
		if prefix < lowest {
			lowest = prefix
		}
	}
	return 1 - lowest
}
