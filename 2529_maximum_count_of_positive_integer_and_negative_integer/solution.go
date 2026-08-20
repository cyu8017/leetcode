// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

func maximumCount(nums []int) int {
	pos, neg := 0, 0
	for _, x := range nums {
		if x > 0 {
			pos++
		} else if x < 0 {
			neg++
		}
	}
	if pos > neg {
		return pos
	}
	return neg
}
