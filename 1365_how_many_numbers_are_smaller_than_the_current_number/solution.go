// LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

import "sort"

func smallerNumbersThanCurrent(nums []int) []int {
	sorted := append([]int(nil), nums...)
	sort.Ints(sorted)
	rank := map[int]int{}
	for i, x := range sorted {
		if _, ok := rank[x]; !ok {
			rank[x] = i
		}
	}
	answer := make([]int, len(nums))
	for i, x := range nums {
		answer[i] = rank[x]
	}
	return answer
}
