// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

import "math"

func judgeSquareSum(c int) bool {
	left, right := 0, int(math.Sqrt(float64(c)))
	for left <= right {
		total := left*left + right*right
		if total == c {
			return true
		}
		if total < c {
			left++
		} else {
			right--
		}
	}
	return false
}
