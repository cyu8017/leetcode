// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

import "sort"

func minMovesToSeat(seats []int, students []int) int {
	sort.Ints(seats)
	sort.Ints(students)
	ans := 0
	for i := range seats {
		d := seats[i] - students[i]
		if d < 0 {
			d = -d
		}
		ans += d
	}
	return ans
}
