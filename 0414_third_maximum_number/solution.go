// LeetCode 0414 - Third Maximum Number
// https://leetcode.com/problems/third-maximum-number/

func thirdMax(nums []int) int {
	first, second, third := 0, 0, 0
	hasFirst, hasSecond, hasThird := false, false, false

	for _, value := range nums {
		if (hasFirst && value == first) || (hasSecond && value == second) ||
			(hasThird && value == third) {
			continue
		}
		if !hasFirst || value > first {
			if hasFirst {
				third = second
				hasThird = hasSecond
			}
			if hasSecond {
				second = first
				hasSecond = true
			}
			first = value
			hasFirst = true
		} else if !hasSecond || value > second {
			if hasSecond {
				third = second
				hasThird = true
			}
			second = value
			hasSecond = true
		} else if !hasThird || value > third {
			third = value
			hasThird = true
		}
	}

	if hasThird {
		return third
	}
	return first
}
