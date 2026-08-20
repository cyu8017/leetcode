// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

func minimumTime(time []int, totalTrips int) int64 {
	mn := time[0]
	for _, t := range time {
		if t < mn {
			mn = t
		}
	}
	lo, hi := int64(1), int64(mn)*int64(totalTrips)
	can := func(mid int64) bool {
		var trips int64
		for _, t := range time {
			trips += mid / int64(t)
			if trips >= int64(totalTrips) {
				return true
			}
		}
		return false
	}
	for lo < hi {
		mid := (lo + hi) / 2
		if can(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
