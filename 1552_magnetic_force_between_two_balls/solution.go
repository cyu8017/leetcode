// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

import "sort"

func maxDistance(position []int, m int) int {
	sort.Ints(position)
	lo, hi := 1, (position[len(position)-1]-position[0])/(m-1)
	for lo <= hi {
		mid := (lo + hi) / 2
		count, last := 1, position[0]
		for _, x := range position[1:] {
			if x-last >= mid {
				count++
				last = x
			}
		}
		if count >= m {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return hi
}
