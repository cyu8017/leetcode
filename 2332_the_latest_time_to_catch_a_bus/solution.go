// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

import "sort"

func latestTimeCatchTheBus(buses []int, passengers []int, capacity int) int {
	sort.Ints(buses)
	sort.Ints(passengers)
	pos := 0
	for _, bus := range buses {
		cap := capacity
		for cap > 0 && pos < len(passengers) && passengers[pos] <= bus {
			pos++
			cap--
		}
		if bus == buses[len(buses)-1] {
			cand := bus
			if cap == 0 {
				cand = passengers[pos-1]
			}
			taken := map[int]bool{}
			for _, p := range passengers {
				taken[p] = true
			}
			for taken[cand] {
				cand--
			}
			return cand
		}
	}
	return -1
}
