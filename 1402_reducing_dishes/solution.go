// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

import "sort"

func maxSatisfaction(satisfaction []int) int {
	sort.Sort(sort.Reverse(sort.IntSlice(satisfaction)))
	total, answer := 0, 0
	for _, value := range satisfaction {
		if total+value <= 0 {
			break
		}
		total += value
		answer += total
	}
	return answer
}
