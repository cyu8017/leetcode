// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/


func repairCars(ranks []int, cars int) int64 {
	ok := func(t int64) bool {
		var done int64
		for _, r := range ranks {
			// cars by mechanic: floor(sqrt(t/r))
			lo, hi := int64(0), int64(cars)
			for lo < hi {
				mid := (lo + hi + 1) / 2
				if r*mid*mid <= t {
					lo = mid
				} else {
					hi = mid - 1
				}
			}
			done += lo
			if done >= int64(cars) {
				return true
			}
		}
		return done >= int64(cars)
	}
	mn := ranks[0]
	for _, r := range ranks {
		if r < mn {
			mn = r
		}
	}
	lo, hi := int64(1), int64(mn)*int64(cars)*int64(cars)
	for lo < hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
