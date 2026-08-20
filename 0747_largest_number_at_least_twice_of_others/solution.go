// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

func dominantIndex(nums []int) int {
	first, second, index := -1, -1, -1
	for i, num := range nums {
		if num > first {
			second = first
			first = num
			index = i
		} else if num > second {
			second = num
		}
	}
	if first >= 2*second {
		return index
	}
	return -1
}
