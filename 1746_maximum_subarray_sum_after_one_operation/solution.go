// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

func maxSumAfterOperation(nums []int) int {
	noSquare := 0
	oneSquare := 0
	best := -1 << 62
	for _, value := range nums {
		withSquare := oneSquare + value
		if noSquare+value*value > withSquare {
			withSquare = noSquare + value*value
		}
		if value*value > withSquare {
			withSquare = value * value
		}
		oneSquare = withSquare
		if noSquare+value > value {
			noSquare = noSquare + value
		} else {
			noSquare = value
		}
		if oneSquare > best {
			best = oneSquare
		}
	}
	return best
}
