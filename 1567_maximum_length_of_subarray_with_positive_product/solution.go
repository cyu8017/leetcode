// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

func getMaxLen(nums []int) int {
	positive, negative, answer := 0, 0, 0
	for _, x := range nums {
		if x == 0 {
			positive, negative = 0, 0
		} else if x > 0 {
			positive++
			if negative > 0 {
				negative++
			} else {
				negative = 0
			}
		} else {
			newPos := 0
			if negative > 0 {
				newPos = negative + 1
			}
			negative = positive + 1
			positive = newPos
		}
		if positive > answer {
			answer = positive
		}
	}
	return answer
}
