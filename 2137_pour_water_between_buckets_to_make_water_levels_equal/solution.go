// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

func equalizeWater(buckets []int, loss int) float64 {
	lo, hi := 0.0, 0.0
	for _, b := range buckets {
		if float64(b) > hi {
			hi = float64(b)
		}
	}
	can := func(x float64) bool {
		var have, need float64
		for _, b := range buckets {
			if float64(b) >= x {
				have += float64(b) - x
			} else {
				need += x - float64(b)
			}
		}
		return have*(1.0-float64(loss)/100.0) >= need
	}
	for iter := 0; iter < 60; iter++ {
		mid := (lo + hi) / 2
		if can(mid) {
			lo = mid
		} else {
			hi = mid
		}
	}
	return lo
}
