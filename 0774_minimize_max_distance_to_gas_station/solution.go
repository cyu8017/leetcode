// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

func minmaxGasDist(stations []int, k int) float64 {
	can := func(dist float64) bool {
		needed := 0
		for i := 1; i < len(stations); i++ {
			needed += int(float64(stations[i]-stations[i-1]) / dist)
		}
		return needed <= k
	}
	lo, hi := 0.0, float64(stations[len(stations)-1]-stations[0])
	for hi-lo > 1e-6 {
		mid := (lo + hi) / 2
		if can(mid) {
			hi = mid
		} else {
			lo = mid
		}
	}
	return hi
}
