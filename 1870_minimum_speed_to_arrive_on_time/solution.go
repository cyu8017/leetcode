// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

func minSpeedOnTime(dist []int, hour float64) int {
	n := len(dist)
	if float64(n-1) >= hour {
		return -1
	}

	canArrive := func(speed int) bool {
		time := 0.0
		for i := 0; i < n-1; i++ {
			time += float64((dist[i] + speed - 1) / speed)
		}
		time += float64(dist[n-1]) / float64(speed)
		return time <= hour
	}

	if !canArrive(10_000_000) {
		return -1
	}

	lo, hi := 1, 10_000_000
	for lo < hi {
		mid := (lo + hi) / 2
		if canArrive(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}
