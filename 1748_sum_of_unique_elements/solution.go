// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

func sumOfUnique(nums []int) int {
	counts := make(map[int]int)
	for _, value := range nums {
		counts[value]++
	}
	total := 0
	for value, count := range counts {
		if count == 1 {
			total += value
		}
	}
	return total
}
