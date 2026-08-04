// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

func distanceBetweenBusStops(distance []int, start int, destination int) int {
	if start > destination {
		start, destination = destination, start
	}
	clockwise := 0
	total := 0
	for i, d := range distance {
		total += d
		if i >= start && i < destination {
			clockwise += d
		}
	}
	if clockwise < total-clockwise {
		return clockwise
	}
	return total - clockwise
}
