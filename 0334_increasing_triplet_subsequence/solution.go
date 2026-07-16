// LeetCode 0334 - Increasing Triplet Subsequence
// https://leetcode.com/problems/increasing-triplet-subsequence/

import "math"

func increasingTriplet(nums []int) bool {
	first := math.MaxInt32
	second := math.MaxInt32
	for _, num := range nums {
		if num <= first {
			first = num
		} else if num <= second {
			second = num
		} else {
			return true
		}
	}
	return false
}
