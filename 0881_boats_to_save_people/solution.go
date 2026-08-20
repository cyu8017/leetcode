// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

import "sort"

func numRescueBoats(people []int, limit int) int {
	sort.Ints(people)
	i, j := 0, len(people)-1
	boats := 0
	for i <= j {
		if people[i]+people[j] <= limit {
			i++
		}
		j--
		boats++
	}
	return boats
}
