// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

import "sort"

func findRadius(houses []int, heaters []int) int {
	sort.Ints(heaters)
	radius := 0
	for _, house := range houses {
		position := sort.SearchInts(heaters, house)
		best := int(1e9)
		if position < len(heaters) {
			distance := heaters[position] - house
			if distance < 0 {
				distance = -distance
			}
			if distance < best {
				best = distance
			}
		}
		if position > 0 {
			distance := heaters[position-1] - house
			if distance < 0 {
				distance = -distance
			}
			if distance < best {
				best = distance
			}
		}
		if best > radius {
			radius = best
		}
	}
	return radius
}
