// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

import "sort"

func carFleet(target int, position []int, speed []int) int {
	type car struct{ pos, spd int }
	cars := make([]car, len(position))
	for i := range position {
		cars[i] = car{position[i], speed[i]}
	}
	sort.Slice(cars, func(i, j int) bool { return cars[i].pos > cars[j].pos })
	fleets := 0
	maxTime := 0.0
	for _, c := range cars {
		time := float64(target-c.pos) / float64(c.spd)
		if time > maxTime {
			fleets++
			maxTime = time
		}
	}
	return fleets
}
